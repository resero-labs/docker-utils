# Issue description

`unattended-upgrades` can cause issues with either Docker or NVidia drivers.
Symptoms include: 

* `NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.`
* Docker deamon not starting

It is believe these are caused when a system library or kernel update clobbers part of the
NVidia or docker libraries or configuration.

# Work-around

Turn off unattended-grades:

1) edit `/etc/apt/apt.conf.d/20auto-upgrades`
2) change `APT::Periodic::Unattended-Upgrade "1";`
3) to `APT::Periodic::Unattended-Upgrade "0";`

# Other possibilities 

Figure out which upgrades seem to impact nvidia and docker and then exclude
those in `/etc/apt/apt.conf.d/50unattended-upgrades`

# Examples of others with similar issues

* [AWS G2 GPU vs. Unattended-upgrade](https://lodge.glasgownet.com/2017/03/21/aws-g2-gpu-vs-unattended-upgrade/comment-page-1/)
* [EC2 cannot reach RDS anymore](https://forums.aws.amazon.com/message.jspa?messageID=774087) (see post on 3/21/2017 @ 12:37pm)
* [Does not support the K520 GRID GPU as used on AWS G2 GPU instances](https://bugs.launchpad.net/ubuntu/+source/nvidia-graphics-drivers-375/+bug/1674666)
* [Tensorflow, CUDA, and CudNN on Ubuntu 16.04 with Titan X](https://aichamp.wordpress.com/category/nvidia/) (mentions disabling unattended-upgrades "so machine does not update the driver")
* [NVIDIA_SMI has failed because it couldn't communicate with the NVIDIA driver](https://devtalk.nvidia.com/default/topic/1000340/cuda-setup-and-installation/-quot-nvidia-smi-has-failed-because-it-couldn-t-communicate-with-the-nvidia-driver-quot-ubuntu-16-04/2)
```
three times happened to me!
my system environment: Ubuntu 16+NVIDIA Driver 384.90
describe: I am sure it could work before, but after some days(maybe 30 days or more), run command "nvidia-smi", it reminds me:"NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running." 
reason：Ubuntu 16 update its kernel automatically! you can check the grub log file, or run command "cat /etc/apt/apt.conf.d/10periodic", you can see the last line:“Unattended-upgrade "1" ”
when the kernel updated, the nvidia driver couldnt work properly.
solution:downgrade the kernel, or select the lower version kernel, or delete the latest version kernel, or set "Unattended-upgrade" as 0, or reinstall the Nvidia driver .
```