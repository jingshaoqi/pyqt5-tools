import os
import shutil


def main():
    build = os.environ['TRAVIS_BUILD_DIR']
    deployed_qt = os.path.join(build, 'deployed_qt')
    package = os.path.join(build, 'pyqt5-tools')

    print('copying {}'.format(deployed_qt))
    print('     to {}'.format(package))
    shutil.copytree(deployed_qt, package)