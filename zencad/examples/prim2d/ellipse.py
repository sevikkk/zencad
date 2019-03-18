#!/usr/bin/env python3
# coding: utf-8

from zencad import *

test_mode()

el_r1 = 7
el_r2 = 5
el_a1 = deg(-45)
el_a2 = deg(180)

m0 = ellipse(r1=el_r1, r2=el_r2)
m1 = ellipse(r1=el_r1, r2=el_r2, angle=(el_a1, el_a2))

m2 = ellipse(r1=el_r1, r2=el_r2, wire=True)
m3 = ellipse(r1=el_r1, r2=el_r2, angle=(el_a1, el_a2), wire=True)

display(m0.right(30 * 0))
display(m1.right(30 * 1))
display(m2.right(30 * 2))
display(m3.right(30 * 3))

show()
