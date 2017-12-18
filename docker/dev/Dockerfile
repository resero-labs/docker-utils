FROM python:3.6.3

# any customization of the image goes here

# setup an *empty* workdir (in this example, arbitrarily chosen to be "/workdir")
# the entrypoint pip installs an editable version of what's in the workdir into the python environment
# workdir is in fact not empty, but is the mount of the project directory into the container
# specified in the dockerutils.cfg for this image
WORKDIR /workdir
ENTRYPOINT /usr/local/bin/pip install -e /workdir && /bin/bash