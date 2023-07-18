#!/usr/bin/python
#-*- coding:utf-8 -*-

from .parser import ConfigParser
import subprocess
import sys

app = 'edge'

def parse_command(config:dict):
    command = [app]
    for key in config:
        command.append(ConfigParser.KEY_MAP[key])
        command.append(config[key])

    return command

def main():
    config_file = sys.prefix + '/etc/start-edge/config.json'

    parser = ConfigParser(config_file)
    config = parser.parse()
    if config is None:
        exit(1)

    command = parse_command(config)
    command.append('-f')
    proc = subprocess.Popen(command)
    status = proc.wait()
    print('edge exit with code: %d' %(status))

if __name__ == '__main__':
    main()

