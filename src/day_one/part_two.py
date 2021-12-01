#!/usr/bin/env python3
count_of_increases = 0
with open("input.txt", "r") as input:
    depths = list(map(lambda x: int(x.strip()), input.readlines()))
    sum_of_previous_depths = None
    for index, depth in enumerate(depths):
        if index + 2 > len(depths) - 1:
            break
        sum_of_current_depths = depths[index] + depths[index + 1] + depths[index + 2]
        if (sum_of_previous_depths is not None) and (
            sum_of_current_depths - sum_of_previous_depths > 0
        ):
            count_of_increases += 1
        sum_of_previous_depths = sum_of_current_depths
print(count_of_increases)
