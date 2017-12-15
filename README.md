# Docker Utilities for Projects that Conform to these Conventions

There are cases in which it is advantageous to build multiple docker images from the same project.
For instance:
* seperating development/test dependencies out of production container, e.g. production container vs. dev/test container
* seperating data science notebook container from execution container
* environment experimentation
* cases in which you want to "freeze" any external dependencies in one container and use that as a base
for containers that are dependent solely on the project

This utility provide an opinionated way of accomplishing this. 

# Conventions

A project that desires to make use of this utility should/can:
1) Create a docker directory tree at the root of the project

    In this directory tree there should be one directory for each unique container that is desired.
    Each of these directories would contain the `Dockerfile` that will be used to create the container
    as well as any source specific to that container.
2) Use versioneer for project versioning. 

    As part of the container build, a file, `_version.py.bld`, will be generated and placed at the project 
    root. A docker file can add that file to the image on creation to prevent the need for including the
    .git directory tree in the container context (usually quite expensive).
3) Utilize built in support for [NVIDIA Docker 2.0](https://github.com/NVIDIA/nvidia-docker) to access GPUs in 
container
4) Create a docker/base directory to make use of built in external dependency isolation capability

    This capability supports environments from which docker build isn't able to access external dependencies,
    i.e. Docker Hub, pypi, etc. A base image can be defined to isolate any dependencies that are required. That
    image can then be built and transfer-image used to transfer the base image to the target environment. 
    Subsequent images can be built based of that image that are "self-contained" (relying only on source
    from the project). The remote docker api can then be used to quickly iterate only requiring the more
    cumbersome transfer-image to be used when external dependencies change.
5) Building and running images controlled through configuration (<project_dir>/docker/run.cfg)

    Includes setting most docker parameters, i.e. volume mounts, ports, networks, commands, etc. with
    replacement varilable support for things like user, project root, etc.  

# Examples     
    
Conventions:
1) There is a docker directory tree at the root of the project
2) Base image convention
3) Derived image conventions
4) Supports GPU via NVIDIA Docker 2.0
5) Multi-stage conventions (as builder)
6) Run configurations captured in <project>/docker/run.cfg
7) replacement variables in volumes, etc
    * user
    * root
    * workdir
8) Environment Variable Conventions
9) Support for versioneer