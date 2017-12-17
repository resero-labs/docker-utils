#!/usr/bin/env python3
import os
import venv


def create_venv(designation):
    env_builder = venv.EnvBuilder(clear=True, prompt=designation, with_pip=True, symlinks=True, system_site_packages=True)
    directory = f".{designation}"
    env_path = os.path.join('/', directory)
    env_builder.create(env_path)
    activate_rel_path = os.path.join('.', directory, 'bin', 'activate')
    symlink_path = os.path.join('/', designation)
    if os.path.exists(symlink_path):
        os.remove(symlink_path)
    os.symlink(activate_rel_path, symlink_path)


if __name__ == "__main__":
    create_venv('cpu-env')
    create_venv('gpu-env')


