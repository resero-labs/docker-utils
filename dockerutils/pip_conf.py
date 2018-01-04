"""Context manager for working with pip configuration"""
import os
from shutil import copy2

# pylint: disable=too-few-public-methods
class pip_conf: # pylint: disable=invalid-name
    """Context manager for using pip.conf.template for pip.conf"""
    def __init__(self, new_path):
        self.new_path = os.path.expanduser(new_path)
        self.pip_conf = os.path.join(self.new_path, 'pip.conf')
        self.pip_copied = False
        self.pip_conf_exists = False

    def __enter__(self):
        self.pip_conf_exists = os.path.exists(self.pip_conf)
        if not self.pip_conf_exists:
            pip_conf_template = os.path.join(self.new_path, 'pip.conf.template')
            if os.path.exists(pip_conf_template):
                self.pip_copied = True
                copy2(pip_conf_template, self.pip_conf)
            else:
                print('No pip.conf found, will not pull packages from custom package manager')

    def __exit__(self, etype, value, traceback):
        if self.pip_copied:
            os.remove(self.pip_conf)
