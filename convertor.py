#!/usr/bin/env python3

import argparse
import importlib

class convertor():

    def __init__(self, source_format, target_format, source_filename, target_filename):
        self.source = importlib.import_module('configurator.configurator_{}'.format(source_format))
        self.target = importlib.import_module('configurator.configurator_{}'.format(target_format))
        self.target.dump(target_filename, self.source.load(source_filename))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert configuration file.')
    parser.add_argument('-s', '--source_format', help='source format', default='python')
    parser.add_argument('-t', '--target_format', help='target format', default='json')
    parser.add_argument('source_filename', help='source filename')
    parser.add_argument('target_filename', help='target filename')
    #parser.print_help()
    args = parser.parse_args()
    #print(args)
    convertor(args.source_format, args.target_format, args.source_filename, args.target_filename)
