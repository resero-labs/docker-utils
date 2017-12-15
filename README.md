# Docker Utilities for Projects that Conform to these Conventions

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