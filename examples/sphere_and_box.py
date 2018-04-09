#!/usr/bin/env python3
#coding: utf-8

import zencad
import zencad.solid as solid
from zencad.widget import *

box = solid.box(300, 200, 100, center = True)
sphere = solid.sphere(100).up(100)

union = box + sphere

display(union)
show()