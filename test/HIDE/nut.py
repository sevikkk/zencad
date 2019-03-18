#!/usr/bin/env python3
# coding: utf-8

from zencad import *

import evalcache

evalcache.enable_diagnostic()


def instrument_metric_nut(drad, step, h):
    H = step * math.tan(deg(60))

    pseg = polysegment(
        points(
            [
                (drad + H / 2, 0, 0),
                (drad - H / 4, 0, -(3 / 8 * step)),
                (drad - H / 4, 0, -(5 / 8 * step)),
                (drad + H / 2, 0, -step),
            ]
        ),
        closed=True,
    )

    path = helix(radius=drad, height=h, step=step)
    base = pipe_shell(path=path, prof=pseg, frenet=True)
    return base


def metric_nut(d, step, h):
    H = step * math.tan(deg(60))
    drad = d / 2 - 3 / 8 * H
    cil = cylinder(r=d / 2, h=h)
    instr = instrument_metric_nut(drad=drad, step=step, h=h + step)
    ret = cil - instr

    return ret


m = (
    metric_nut(8, 1.25, 30).up(25.3)
    + cylinder(r=8 / 2, h=20).up(5.3)
    + linear_extrude(ngon(r=7.1, n=6), (0, 0, 5.3))
)

display(m)
show()
