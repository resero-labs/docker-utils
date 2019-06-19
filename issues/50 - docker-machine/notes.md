# Consider replacing some functionality with `docker-machine`

The following are steps I used to get `docker-machine` to work for the `create-dock` use case:

1) create a security group named `docker-machine`
    
    Create inbound access for port 22 and 2376 (docker daemon) with 
    appropriate cidr blocks (in our case: 198.60.24.141/32, 10.93.0.0/16 and 208.86.202.9/32)
    
    Do this because `docker-machine` opens up ssh and docker daemon port to the world by default
    and we don't want to do this.
    
2) make sure your `~/.ssh/config` file isn't setting conflicting information

    By default we'll let `docker-machine` generate a keypair and use that, so don't
    specify an IdentityFile for the ip block that you'll be using with `docker-machine`

3) try `docker-machine create`

    Here is the command line I used: `aws-vault exec resero -- docker-machine create --driver amazonec2 --amazonec2-region us-west-2  --amazonec2-subnet-id subnet-6c555b25  --amazonec2-vpc-id vpc-6298c405 --amazonec2-zone b --amazonec2-security-group-readonly --amazonec2-use-private-address dm-test`
    
    Along with the reasons for the various options:
    
    * `--amazonec2-subnet-id subnet-6c555b25` - because default subnet is out of ips
    * `--amazonec2-vpc-id vpc-6298c405` - because if you specify a subnet you need to also specify the vpc
    * `--amazonec2-zone b` - also required with subnet and vpc
    * `--amazonec2-security-group-readonly` - (see step 1) this prevents `docker-machine` from opening 22 and 2376 to the world
    * `--amazonec2-use-private-address` - otherwise `docker-machine` will attempt to use the public IP for the ec2 instance, and that doesn't work with our network config
    
## Things to be aware of

### AWS-Vault
Because AWS credentials are in env variables when running the above, those credentials are 
captured in the `~/.docker/machine/machines/dm-test/config.json` file. Because the `aws-vault` credentials
expire, `docker-machine` will stop working after credential expiration.

As a work around, you can remove the applicable lines from the `config.json` and it will work

### ssh access to `dockerd`

Recently, `dockerd` has been exposed via ssh ([docker/cli Issue 1014](https://github.com/docker/cli/pull/1014) and [Docker Tips: Access the DOcker Daemon via SSH](https://medium.com/better-programming/docker-tips-access-the-docker-daemon-via-ssh-97cd6b44a53)).

There is something in how `docker-machine` configures `dockerd` that prevents this from working.

First, modify `~/.ssh/config` to include:

```
Host 10.93.128.135
    User ubuntu
    UserKnownHostsFile=/dev/null
    StrictHostKeyChecking no
    IdentityFile /Users/drapp/.docker/machine/machines/dm-test/id_rsa
```

Then run:

`docker -H ssh://10.93.128.135 images`

This results in:

`Cannot connect to the Docker daemon at http://docker. Is the docker daemon running?`

```
docker -H ssh://10.93.128.97 images       --  0.03s user 0.02s system 2% cpu 2.261 total
docker -H tcp://10.93.128.97:2377 images  --  0.04s user 0.02s system 7% cpu 0.813 total

docker -H ssh://10.93.128.97 run -ti alpine echo “hello”       -- 0.05s user 0.04s system 1% cpu 7.095 total
docker -H tcp://10.93.128.97:2377 run -ti alpine echo “hello”  -- 0.05s user 0.10s system 4% cpu 2.959 total
```