FROM python:3.6.3

# any customization of the image goes here

# to avoid adding .git to the Docker context, but still capture version information, overwrite
# the _version.py file
ADD ./_version.py.bld /workdir/dockerutils/_version.py

# entry point required for CI/CD purposes