#!/usr/bin/env bash

# configure docker:
# put ubuntu user in docker group
# remove unix socket from docker config (we are going to allow TLS network sockets only)
# all key/cert setup is in register-dock script
sudo usermod -aG docker ubuntu
sudo systemctl stop docker

# remove the -H option from the docker service configuration
#
# some versions of docker have the line:
# ExecStart=/usr/bin/dockerd -H fd://
# others have the line:
# ExecStart=/usr/bin/dockerd -H unix://
#
if grep -q "/usr/bin/dockerd -H fd://" /lib/systemd/system/docker.service; then
    sudo sed -i 's"dockerd\ -H\ fd://"dockerd"g' /lib/systemd/system/docker.service
fi
if grep -q "/usr/bin/dockerd -H unix://" /lib/systemd/system/docker.service; then
    sudo sed -i 's"dockerd\ -H\ unix://"dockerd"g' /lib/systemd/system/docker.service
fi

sudo systemctl daemon-reload
sudo systemctl start docker
