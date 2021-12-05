#!/usr/bin/env python3
from functools import reduce
from collections import namedtuple

PosAndAim = namedtuple("PosAndAim", "x y aim")
DirAndMov = namedtuple("DirAndMov", "dir mov")


def calculate_position(pos_and_aim, dir_and_mov):
    if dir_and_mov.dir == "forward":
        return PosAndAim(
            pos_and_aim.x + dir_and_mov.mov,
            pos_and_aim.y + pos_and_aim.aim * dir_and_mov.mov,
            pos_and_aim.aim,
        )
    elif dir_and_mov.dir == "up":
        return PosAndAim(
            pos_and_aim.x, pos_and_aim.y, pos_and_aim.aim - dir_and_mov.mov
        )
    else:
        return PosAndAim(
            pos_and_aim.x, pos_and_aim.y, pos_and_aim.aim + dir_and_mov.mov
        )


with open("input.txt") as input:
    movements = map(
        lambda x: DirAndMov(x.strip().split(" ")[0], int(x.strip().split(" ")[1])),
        input.readlines(),
    )
    pos_and_aim = reduce(calculate_position, movements, PosAndAim(0, 0, 0))
    print(pos_and_aim.x * pos_and_aim.y)
