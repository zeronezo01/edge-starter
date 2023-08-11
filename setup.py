from setuptools import setup, find_packages
from setuptools.command.install import install
from glob import glob
import sys
import os
import subprocess

N2N_PATH = 'n2n' + os.sep

'''def get_virtualenv_path():
    """Used to work out path to install compiled binaries to."""
    if hasattr(sys, 'real_prefix'):
        return sys.prefix

    if hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix:
        return sys.prefix

    if 'conda' in sys.prefix:
        return sys.prefix

    return None'''

class N2ninstall(install):
    def run(self):
        #venv = get_virtualenv_path()
        cmake_cmd = 'cmake ..'
        make_cmd = 'make'
        make_install_cmd = 'make install'
        if not os.path.exists(N2N_PATH + 'build'):
            os.mkdir(N2N_PATH + 'build')

        cmake_dir = os.getcwd() + os.sep + N2N_PATH + 'build'
        subprocess.check_call(cmake_cmd, cwd = cmake_dir, shell = True)
        subprocess.check_call(make_cmd, cwd = cmake_dir, shell = True)
        subprocess.check_call(make_install_cmd, cwd = cmake_dir, shell = True)
        super().run()

requirements = open('requirements.txt').readlines()

setup(
    name = 'start-edge',
    version = '0.1',
    description = 'service to start n2n edge with config file',
    author = 'zerone',
    author_email = 'zeronezo01@163.com',
    packages = find_packages(),
    data_files = [
        (sys.prefix + '/etc/start-edge', ['config/config.json']),
        ('/usr/lib/systemd/system', glob('service/*.service'))
    ],
    install_requires = requirements,
    entry_points = {
        'console_scripts':[
            'start-edge=start_edge.edge:main'
        ]
    },
    cmdclass={'install': N2ninstall}
)
