# Notes on using the AWS DL AMI as the base image

We are using verison 21.0 (ami-0b294f219d14e6a82) currently, but have modified it (by hand) to create our base image
The modifications are as follows:

1) ssh into image
2) Wait for /var/log/unattended-upgrades/unattended-upgrades.log to emit a line
that looks like: `2019-01-24 17:52:10,320 INFO All upgrades installed` (should be aobut 15 minutes)
3) reboot
4) run upgrade.sh script

Because this takes such a long time, go ahead and create an image from this instance
and use that as the base instead of building it into the packer script.

Optionally, we may want to consider running the upgrade-docker script in this 
directory, but we are not currently doing so.

## Watch for updates
[Deep Learning AMI (Ubuntu)](https://aws.amazon.com/marketplace/pp/B077GCH38C)
