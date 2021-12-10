#!/usr/bin/env python3
from fluentpy import _
from collections import namedtuple
from functools import reduce

Position = namedtuple("Position", ["y", "x"])


def try_resolve_position_to_height(position):
    try:
        return rows[position.y][position.x]
    except:
        return None


def resolve_position_to_height(position):
    return rows[position.y][position.x]


def determine_basin(current_neighbours, basin):
    current_neighbours = list(
        filter(
            lambda pos: try_resolve_position_to_height(pos) != 9
            and try_resolve_position_to_height(pos) is not None,
            current_neighbours,
        )
    )
    if not current_neighbours:
        return basin

    new_neighbours = []
    for neighbour in current_neighbours:
        up_down = [neighbour.y - 1, neighbour.y + 1]
        left_right = [neighbour.x - 1, neighbour.x + 1]

        for vert in up_down:
            if vert < 0:
                continue
            try:
                if (Position(vert, neighbour.x) not in basin) and Position(
                    vert, neighbour.x
                ) not in new_neighbours:
                    new_neighbours.append(Position(vert, neighbour.x))
            except:
                continue

        for hor in left_right:
            if hor < 0:
                continue
            try:
                if (
                    Position(neighbour.y, hor) not in basin
                    and Position(neighbour.y, hor) not in new_neighbours
                ):
                    new_neighbours.append(Position(neighbour.y, hor))
            except:
                continue

    basin.extend(current_neighbours)
    return determine_basin(new_neighbours, basin)


with open("input.txt") as input:
    global rows
    rows = (
        _(input.readlines())
        .map(lambda x: _(list(x.strip())).map(lambda y: int(y)).to(list))
        .to(list)
    )

    basins = []
    for y, row in enumerate(rows):
        for x, col in enumerate(row):
            height = resolve_position_to_height(Position(y, x))

            neighbours = []
            up_down = [y - 1, y + 1]
            left_right = [x - 1, x + 1]

            for vert in up_down:
                if vert < 0:
                    continue
                try:
                    neighbours.append(Position(vert, x))
                except:
                    continue

            for hor in left_right:
                if hor < 0:
                    continue
                try:
                    neighbours.append(Position(y, hor))
                except:
                    continue

            # we've found a basin starting point
            if height < min(
                filter(
                    lambda z: z is not None,
                    map(try_resolve_position_to_height, neighbours),
                )
            ):
                basins.append(determine_basin(neighbours, [Position(y, x)]))

    lens = map(lambda x: len(x), sorted(basins, key=lambda x: len(x), reverse=True)[:3])
    print(reduce(lambda acc, x: x * acc, lens, 1))
