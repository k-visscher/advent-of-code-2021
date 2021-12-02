#!/usr/bin/env python3
horizontal_position = 0
vertical_position = 0
aim = 0
with open("input.txt") as input:
    movements = list(
        map(
            lambda x: (x.strip().split(" ")[0], int(x.strip().split(" ")[1])),
            input.readlines(),
        )
    )
    for movement in movements:
        if movement[0] == "forward":
            horizontal_position += movement[1]
            vertical_position += aim * movement[1]
        elif movement[0] == "up":
            aim -= movement[1]
        else:
            aim += movement[1]

print(horizontal_position * vertical_position)
