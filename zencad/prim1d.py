import pyservoce
from zencad.lazifier import lazy, shape_generator, nocached_shape_generator

from zencad.util import points, point3


@lazy.lazy(cls=nocached_shape_generator)
def segment(pnt0, pnt1):
    return pyservoce.segment(pyservoce.point3(pnt0), pyservoce.point3(pnt1))


@lazy.lazy(cls=shape_generator)
def polysegment(lst, closed=False):
    return pyservoce.polysegment(points(lst), closed)


@lazy.lazy(cls=nocached_shape_generator)
def circle_arc(p1, p2, p3):
    """Построение дуги круга по трем точкам"""
    return pyservoce.circle_arc(point3(p1), point3(p2), point3(p3))


@lazy.lazy(cls=shape_generator)
def helix(r, h, step, angle=0, left=False):
    # return make_helix(*args, **kwargs)
    return pyservoce.long_helix(
        radius=r, height=h, step=step, angle=angle, leftHanded=left
    )
