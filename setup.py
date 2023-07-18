from setuptools import setup, find_packages
import sys
from glob import glob

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
    }
)
