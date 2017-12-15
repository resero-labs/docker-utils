from .cd import cd
from .pip_conf import pip_conf
from .image_conventions import get_root_dir, get_default_project_name, get_image_name, get_image_tag, \
    get_image_types, get_default_image_name
from .gen_version import gen_version_file

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
