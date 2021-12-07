#!/usr/bin/env python3
from fluentpy import _
from collections import Counter

with open("input.txt") as input:
    positions = _(input.readline()).strip().split(",").map(lambda x: int(x))._
    occurences = dict(Counter(positions))

    costs = []
    for i in range(min(occurences.keys()), max(occurences.keys()) + 1):
        costs.append(
            _(occurences)
            .items()
            .filter(lambda x: x[0] != i)
            .map(lambda x: sum(range(1, abs(i - x[0]) + 1)) * x[1])
            .sum()
            ._
        )
    print(_(costs).sorted()._[0])
