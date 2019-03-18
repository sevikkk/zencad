#!/usr/bin/env python3
# coding: utf-8

from zencad import *

lazy.diag = True
# lazy.diag_values = True
# lazy.print_invokes = True


@lazy
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


@lazy
def metric_nut(d, step, h):
    H = step * math.tan(deg(60))
    drad = d / 2 - 3 / 8 * H
    cil = cylinder(r=d / 2, h=h)
    instr = instrument_metric_nut(drad=drad, step=step, h=h + step)
    ret = cil - instr

    return ret


nut = metric_nut(8, 1.25, 50)

nut = (
    nut.up(15.3)
    + cylinder(r=8 / 2, h=10).up(5.3)
    + linear_extrude(ngon(r=7.1, n=6), (0, 0, 5.3))
)


fontpath = "/home/mirmik/project/privdocs/bujin/poster/fonts/mandarinc.ttf"
m = textshape("ZenCad", fontpath, 20)

w = 64.68
h = 13.5
m = m.extrude(7) + box(w, h, 1.5)

base = rectangle(w, h, wire=True)
base2 = rectangle(w + 5 * 2, h + 5 * 2, wire=True).back(5).left(5).down(10)

trans = up(10) * forw(5) * right(5)
base = loft([base, base2])
base = base.transform(trans)

nut1 = nut.rotateY(deg(90)).back(5).right((w + 5 * 2 - 65.3) / 2).up(11)
nut2 = nut.rotateX(deg(90)).right(w / 2 + 5).forw(30).up(11)

# nut = nut1
m = m.transform(trans)
base = base + nut1.forw(5 + h / 2 + 5)
m3 = m.forw(h * 1.5)
m = m - base
m2 = m.rotateX(deg(180)).up(20)

# nut = nut.rotateX(deg(90)).forw(65.3/2).rotateZ(deg(50))
# nut = nut + nut.rotateZ(deg(-100))

# nuttrans = translate(10,35,5) * rotateZ(deg(50)) * rotateX(deg(90))
# nuttrans2 = translate(10+65,35,5) * rotateZ(deg(-50)) * rotateX(deg(90))
# nut1 = nut.transform(nuttrans) - base
# nut2 = nut.transform(nuttrans2) - base
# nut = nut1 + nut2
# nut = nut.translate(w/2+5, h/2+5, 5) - base

scn = Scene()

scn.add(base.unlazy())
scn.add(m.unlazy(), Color(1, 1, 1))
scn.add(m2.unlazy(), Color(1, 1, 1))
scn.add(m3.unlazy(), Color(1, 1, 1))
# scn.add(nut.unlazy())
# scn.add(nut2.unlazy())

show(scn)
