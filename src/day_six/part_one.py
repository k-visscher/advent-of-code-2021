#!/usr/bin/env python3
from functools import reduce
from collections import namedtuple


def cycle_days(lantern_fishes, days):
    print(days)
    if days == 0:
        return lantern_fishes
    else:
        return cycle_days(cycle_day(lantern_fishes), days - 1)


def cycle_day(lantern_fishes):
    born_latern_fishes = len(
        list(filter(lambda lantern_fish: lantern_fish == 0, lantern_fishes))
    )
    cycled_latern_fishes = list(
        map(
            lambda lantern_fish: lantern_fish - 1 if lantern_fish != 0 else 6,
            lantern_fishes,
        )
    )
    return cycled_latern_fishes + ([8] * born_latern_fishes)


with open("input.txt") as input:
    lantern_fishes = list(map(lambda x: int(x), input.readline().strip().split(",")))
    lantern_fishes = len(cycle_days(lantern_fishes, 80))
    print(lantern_fishes)
