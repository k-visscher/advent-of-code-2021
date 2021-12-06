#!/usr/bin/env python3
from collections import Counter


def create_or_add(dict, key, value):
    try:
        dict[key] += value
    except:
        dict[key] = value


def cycle_days(lantern_fishes, days):
    if days == 0:
        return lantern_fishes
    else:
        return cycle_days(cycle_day(lantern_fishes), days - 1)


def cycle_day(current_day):
    next_day = dict()
    for key, val in current_day.items():
        if key == 0:
            create_or_add(next_day, 8, val)
            create_or_add(next_day, 6, val)
        else:
            create_or_add(next_day, key - 1, val)
    return next_day


with open("input.txt") as input:
    lantern_fishes = map(lambda x: int(x), input.readline().strip().split(","))
    first_day = dict(Counter(lantern_fishes))
    last_day = cycle_days(first_day, 256)
    print(sum(last_day.values()))
