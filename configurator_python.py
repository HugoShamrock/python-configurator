#!/usr/bin/env python3

import imp
import os

def load(filename):
    if os.path.exists(filename):
        module = imp.load_source('virtual', filename)
        config = {
            i: getattr(module, i)
            for i in dir(module)
            if not i.startswith('__') and not i.endswith('__')
        }
        return config
