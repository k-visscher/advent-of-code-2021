#!/usr/bin/env python3
from functools import reduce
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
Line = namedtuple("Line", ["start", "end"])


def flatten(x):
    return [item for sublist in x for item in sublist]


def max_x(acc, line):
    if line.start.x > acc:
        return line.start.x
    elif line.end.x > acc:
        return line.end.x
    else:
        return acc


def max_y(acc, line):
    if line.start.y > acc:
        return line.start.y
    elif line.end.y > acc:
        return line.end.y
    else:
        return acc


def add_line_to_diagram(line, diagram):
    horizontal = line.start.y == line.end.y

    if horizontal:
        for i in (
            range(line.start.x, line.end.x + 1)
            if line.end.x == max(line.start.x, line.end.x)
            else range(line.end.x, line.start.x + 1)
        ):
            diagram[line.start.y][i] += 1
    else:
        for i in (
            range(line.start.y, line.end.y + 1)
            if line.end.y == max(line.start.y, line.end.y)
            else range(line.end.y, line.start.y + 1)
        ):
            diagram[i][line.start.x] += 1


with open("input.txt") as input:
    lines = map(
        lambda x: Line(x[0], x[1]),
        map(
            lambda x: [
                Point(
                    int(raw_point.strip().split(",")[0]),
                    int(raw_point.strip().split(",")[1]),
                )
                for raw_point in x.split("->")
            ],
            input.readlines(),
        ),
    )
    lines = list(
        filter(
            lambda line: line.start.x == line.end.x or line.start.y == line.end.y, lines
        )
    )

    max_x = reduce(max_x, lines, 0)
    max_y = reduce(max_y, lines, 0)

    diagram = [[0] * (max_x + 1) for _ in range(max_y + 1)]
    for line in lines:
        add_line_to_diagram(line, diagram)

    count_of_at_least_two_intersections = len(
        list(filter(lambda x: x >= 2, flatten(diagram)))
    )
    print(count_of_at_least_two_intersections)
