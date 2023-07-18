#-*- coding:utf-8 -*-

import json
import random

class ConfigParser:

    KEY_MAC = 'mac'

    KEY_MAP = {
            'address': '-a',
            'key': '-k',
            'community': '-c',
            'super-node': '-l',
            'mac': '-m'
            }

    def __init__(self, path):
        self.path = path

    # generate random mac to edge, second byte need to be even number
    def __generate_mac(self):
        i = 0
        mac = ''
        while i < 12:
            num = 0
            if i == 1:
                num = random.randint(0, 7) * 2
            else :
                num = random.randint(0, 15)
            mac += hex(num)[2]
            if i % 2 == 1 and i != 11:
                mac += ':'

            i += 1

        return mac

    def parse(self):
        data = None
        with open(self.path) as config_file:
            data = json.load(config_file)

        if data != None:
            data[ConfigParser.KEY_MAC] = self.__generate_mac()

        return data
