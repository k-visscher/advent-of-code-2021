#!/usr/bin/env python3
from functools import reduce

with open("input.txt") as input:
    depths = list(map(lambda x: int(x.strip()), input.readlines()))
    count_of_increases = reduce(
        lambda acc, x: acc + 1 if x[1] - x[0] > 0 else acc, zip(depths, depths[1:]), 0
    )
    print(count_of_increases)
