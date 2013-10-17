#!/usr/bin/env python3

import pickle
import os

def load(filename):
    if os.path.exists(filename):
        with open(filename, mode='rb') as f:
            return pickle.load(f)

def dump(filename, config, protocol=0):
    with open(filename, mode='wb') as f:
        pickle.dump(config, f, protocol)
