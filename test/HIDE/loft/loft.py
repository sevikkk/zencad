#!/usr/bin/env python3
# coding: utf-8

import sys

sys.path.insert(0, "../..")

import zencad.solid as solid
from zencad.widget import *

b = solid.box(67, 89, 56)

display(b)
show()
