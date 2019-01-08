#!/usr/bin/env bash

# install dependencies
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gcc \
    make \
    python3 \
    python3-pip \
    software-properties-common
pip3 install awscli --upgrade --user

# get the latest nvidia drivers and install them
wget -qP /tmp http://us.download.nvidia.com/tesla/410.79/NVIDIA-Linux-x86_64-410.79.run
chmod +x /tmp/NVIDIA-Linux-x86_64-410.79.run
sudo /tmp/NVIDIA-Linux-x86_64-410.79.run -silent

# now get docker and nvidia-docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update
sudo apt-get install -y docker-ce \
    nvidia-docker2

# configure docker:
# put ubuntu user in docker group
# remove unix socket from docker config (we are going to allow TLS network sockets only)
# key/cert setup is in register-dock
sudo usermod -aG docker ubuntu
sudo systemctl stop docker
sudo sed -i 's"dockerd\ -H\ unix://"dockerd"g' /lib/systemd/system/docker.service
sudo systemctl daemon-reload
sudo systemctl start docker

# disable unattended-updates
# kernel updates, though infrequent, can mess up both the docker daemon and the nvidia drivers
# rather than doing unattended-updates, we should periodically update the AMI by simply rebuilding
# the image
sudo sed -i 's/APT::Periodic::Unattended-Upgrade "1";/APT::Periodic::Unattended-Upgrade "0";/g' /etc/apt/apt.conf.d/20auto-upgrades
