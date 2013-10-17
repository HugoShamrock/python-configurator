#!/usr/bin/env python3

import sys
import importlib

class convertor():

    def __init__(self, source_module, target_module, source_filename, target_filename):
        self.source = importlib.import_module('configurator.configurator_{}'.format(source_module))
        self.target = importlib.import_module('configurator.configurator_{}'.format(target_module))
        self.target.dump(target_filename, self.source.load(source_filename))

if __name__ == '__main__':
    if len(sys.argv) == 5:
        convertor(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print('usage: {} <source_module> <target_module> <source_filename> <target_filename>'.format(sys.argv[0]))
