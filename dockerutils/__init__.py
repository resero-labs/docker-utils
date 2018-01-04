"""
A collection of utility functions and classes used by the xxx-image scripts
"""
from .cd import cd
from .pip_conf import pip_conf
from .image_conventions import get_root_dir, get_image_types, get_image_designation
from .gen_version import gen_version_file

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
