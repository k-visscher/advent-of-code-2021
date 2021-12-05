#!/usr/bin/env python3
from functools import reduce

with open("input.txt") as input:
    movements = list(
        map(
            lambda x: (x.strip().split(" ")[0], int(x.strip().split(" ")[1])),
            input.readlines(),
        )
    )
    horizontal_position = reduce(
        lambda acc, x: acc + x[1] if x[0] == "forward" else acc, movements, 0
    )
    vertical_position = reduce(
        lambda acc, x: acc + x[1] if x[0] == "down" else acc - x[1],
        filter(lambda x: x[0] == "down" or x[0] == "up", movements),
        0,
    )
    print(horizontal_position * vertical_position)
