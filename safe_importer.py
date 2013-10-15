#!/usr/bin/env python3

import sys
import os

while True:
    try:
        sys.path.remove(os.getcwd())
    except:
        break
