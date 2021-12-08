#!/usr/bin/env python3
from fluentpy import _

num_to_seg = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}

with open("input.txt") as input:
    print(
        _(input.readlines())
        .map(
            lambda x: _(x.split("|")[1].strip().split(" "))
            .map(lambda y: len(y))
            .to(list)
        )
        .flatten()
        .filter(
            lambda x: x in [num_to_seg[1], num_to_seg[4], num_to_seg[7], num_to_seg[8]]
        )
        .len()
        ._
    )
