import os
from shutil import copy2

class pip_conf:
    """Context manager for using pip.conf.template for pip.conf"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)
        self.pip_conf = os.path.join(self.newPath, 'pip.conf')
        self.pip_copied = False

    def __enter__(self):
        self.pip_conf_exists = os.path.exists(self.pip_conf)
        if not self.pip_conf_exists:
            pip_conf_template = os.path.join(self.newPath, 'pip.conf.template')
            if os.path.exists(pip_conf_template):
                self.pip_copied = True
                copy2(pip_conf_template, self.pip_conf)
            else:
                print('No pip.conf found, will not pull packages from custom package manager')

    def __exit__(self, etype, value, traceback):
        if self.pip_copied:
            os.remove(self.pip_conf)
