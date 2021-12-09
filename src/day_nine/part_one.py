#!/usr/bin/env python3
from fluentpy import _

with open("input.txt") as input:
    rows = (
        _(input.readlines())
        .map(lambda x: _(list(x.strip())).map(lambda y: int(y)).to(list))
        .to(list)
    )

    low_points = []
    for y, row in enumerate(rows):
        for x, col in enumerate(row):
            height = rows[y][x]

            neighbours = []
            up_down = [y - 1, y + 1]
            left_right = [x - 1, x + 1]

            for vert in up_down:
                if vert < 0:
                    continue
                try:
                    neighbours.append(rows[vert][x])
                except:
                    continue

            for hor in left_right:
                if hor < 0:
                    continue
                try:
                    neighbours.append(rows[y][hor])
                except:
                    continue

            if height < min(neighbours):
                low_points.append(height)

    print(sum(_(low_points).map(lambda x: x + 1)._))
