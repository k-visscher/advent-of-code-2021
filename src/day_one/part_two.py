#!/usr/bin/env python3
count_of_increases = 0
with open("input.txt") as input:
    depths = list(map(lambda x: int(x.strip()), input.readlines()))
    sum_of_previous_depths = None
    for index in range(0, len(depths) - 2):
        sum_of_current_depths = sum(depths[index : index + 3])
        if (sum_of_previous_depths is not None) and (
            sum_of_current_depths - sum_of_previous_depths > 0
        ):
            count_of_increases += 1
        sum_of_previous_depths = sum_of_current_depths
print(count_of_increases)
