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
    vertical = line.start.x == line.end.x

    if horizontal:
        for i in (
            range(line.start.x, line.end.x + 1)
            if line.end.x == max(line.start.x, line.end.x)
            else range(line.end.x, line.start.x + 1)
        ):
            diagram[line.start.y][i] += 1
    elif vertical:
        for i in (
            range(line.start.y, line.end.y + 1)
            if line.end.y == max(line.start.y, line.end.y)
            else range(line.end.y, line.start.y + 1)
        ):
            diagram[i][line.start.x] += 1
    else:
        # diagonal
        #
        # from top left to bottom right
        # \
        # \
        #  x
        # from bottom right to top left
        # x
        # \
        #  \
        if (line.start.x < line.end.x and line.start.y < line.end.y) or (
            line.start.x > line.end.x and line.start.y > line.end.y
        ):
            x_range = (
                range(line.start.x, line.end.x + 1)
                if line.end.x == max(line.start.x, line.end.x)
                else range(line.end.x, line.start.x + 1)
            )
            y_range = (
                range(line.start.y, line.end.y + 1)
                if line.end.y == max(line.start.y, line.end.y)
                else range(line.end.y, line.start.y + 1)
            )
            for pos in zip(x_range, y_range):
                diagram[pos[1]][pos[0]] += 1
        # from bottom left to top right
        #  x
        # /
        # /
        # from bottom right to top left
        #  /
        # /
        # x
        else:
            x_range = None
            y_range = None

            x_diff = abs(line.end.x - line.start.x)
            y_diff = abs(line.start.y - line.end.y)

            if line.start.x < line.end.x:
                x_range = list(range(line.start.x, line.start.x + x_diff + 1))
                y_range = list(range(line.start.y, line.start.y - y_diff - 1, -1))
            else:
                x_range = list(range(line.start.x, line.start.x - x_diff - 1, -1))
                y_range = list(range(line.start.y, line.start.y + y_diff + 1))

            for pos in zip(x_range, y_range):
                diagram[pos[1]][pos[0]] += 1


with open("input.txt") as input:
    lines = list(
        map(
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
