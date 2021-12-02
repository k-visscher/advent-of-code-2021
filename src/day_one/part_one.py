#!/usr/bin/env python3
count_of_increases = 0
with open("input.txt") as input:
    depths = list(map(lambda x: int(x.strip()), input.readlines()))
    previous_depth = None
    for current_depth in depths:
        if (previous_depth is not None) and (current_depth - previous_depth > 0):
            count_of_increases += 1
        previous_depth = current_depth
print(count_of_increases)
