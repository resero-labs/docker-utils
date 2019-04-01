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