import logging
import os
import getpass

logger = logging.getLogger(__name__)


_ROOT_DIR = None
def get_root_dir():
    global _ROOT_DIR
    '''
    get_root_dir will return the root directory of the project that contains a docker file.
     The constraints for our project with regard to docker are that there id a docker directoy as
     a top level sub-directory under the project root. The project root directory name is the base
     name of the docker file. There are sub-directories under docker that serve as the modes of
     various docker files that will be build (e.g. dev, lanista, jenkins, etc.)
    :return: root_directory for docker builda
    '''

    if _ROOT_DIR is None:
        docker_dir = os.path.join(os.getcwd(), 'docker')
        if os.path.exists(docker_dir) and os.path.isdir(docker_dir):
            _ROOT_DIR = os.getcwd()
        else:
            logger.warning('Unable to find docker directory. Invalid root: ' + os.getcwd())

    return _ROOT_DIR

def get_default_project_name():
    return os.path.basename(get_root_dir()).lower()


def get_image_name(project, mode, image_name=None):
    if mode == 'shell' or mode == 'shell-nohist':
        return image_name or '{}-{}'.format(project, 'base')
    return image_name or '{}-{}'.format(project, mode)


def get_image_tag(mode):
    if mode == 'base' or mode == 'shell' or mode == 'shell-nohist':
        return 'latest'
    return os.getenv('IMAGE_TAG') or getpass.getuser()


def get_image_types(synthetic_images=[]):
    docker_dir = os.path.join(get_root_dir(), 'docker')
    return [x for x in os.listdir(docker_dir) if os.path.isdir(os.path.join(docker_dir, x))].append(synthetic_images)


def get_default_image_name(mode):
    return get_image_name(get_default_project_name(), mode)

