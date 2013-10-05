#!/usr/bin/env python
from __future__ import division
import sys

def drawpbar(val, m):
    ratio = val / m
    sys.stdout.write('\r[{0: <50}]{1: >4.0%}'.format('#' * int(ratio * 50), ratio))
    sys.stdout.flush()
