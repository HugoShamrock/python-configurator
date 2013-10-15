#!/usr/bin/env python3

import sys
from configurator.convertor import convertor

class python2json(convertor):

    from configurator import configurator_python as source
    from configurator import configurator_json as target

if __name__ == '__main__':
    if len(sys.argv) == 3:
        python2json(sys.argv[1], sys.argv[2])
    else:
        print('usage: {} <source_filename> <target_filename>'.format(sys.argv[0]))
