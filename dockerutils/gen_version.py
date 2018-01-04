"""
Holds the function to generate a version file, used to 'transplant'
version into docker container
"""
import json
import sys
from importlib import import_module
from . import get_root_dir

def gen_version_file(filename='_version.py.bld'):
    """
    Generates a versioneer version file that can be used in
    situations in which the scm is not available (usually
    in docker container).
    :param filename: filename for the generated version file
    :return: None
    """
    orig_path = sys.path
    new_path = [get_root_dir()]
    new_path.extend(orig_path)
    sys.path = new_path
    try:
        versioneer_module = import_module('versioneer')
        version = versioneer_module.get_versions()
    except ImportError:
        version = '0.0.0'

    sys.path = orig_path
    with open(filename, 'w') as text_file:
        text_file.write("""
# This file was generated by build-image invoking versioneer.py. It is generated
# from revision-control system data and simulates the pre-generated copy of this
# file produced by Versioneer for distribution tarballs.

import json

version_json = '''
{}
'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)

""".format(json.dumps(version, sort_keys=True, indent=4, separators=(',', ': '))))
