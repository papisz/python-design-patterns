#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Simple Strategy Pattern example."""


def triangle_area(base, height):
    u"""Calculate the area of a Δ."""
    return 0.5*base*height


def parallelogram_area(base, height):
    u"""Calculate the area of a ▱."""
    return base*height


class Shape(object):

    """Just a basic container for our shapes."""

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def __repr__(self):
        return "base = {}, height = {}".format(self.base, self.height)


if __name__ == "__main__":
    data = [Shape(base=1, height=2), Shape(base=2, height=3),
            Shape(base=3, height=3)]

    print u"Calculating Δ (triangle) area..."
    area_calculator = triangle_area

    for d in data:
        print d, "Area =", area_calculator(base=d.base, height=d.height)

    print u"Calculating ▱ (parallelogram) area..."
    area_calculator = parallelogram_area

    for d in data:
        print d, "Area =", area_calculator(base=d.base, height=d.height)
