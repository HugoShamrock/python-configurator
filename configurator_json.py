#!/usr/bin/env python3

import json
import os

def read(filename):
    if os.path.exists(filename):
        with open(filename, mode='r') as f:
            return json.load(f)

def write(filename, config):
    with open(filename, mode='w') as f:
        json.dump(config, f, indent=2)
