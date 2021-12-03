#!/usr/bin/env python3
def calculate(bytes, compare, predicate):
    for i in range(0, len(bytes[0])):
        count_of_zero = 0
        count_of_one = 0

        for byte in bytes:
            count_of_zero += int(byte[i] == "0")
            count_of_one += int(byte[i] == "1")

        x = compare(count_of_zero, count_of_one)
        bytes = [
            byte for byte in bytes if predicate(byte[i], x, count_of_zero, count_of_one)
        ]
        if len(bytes) == 1:
            break

    return int(bytes[0], base=2)


with open("input.txt") as f:
    bytes = list(map(lambda x: x.strip(), f.readlines()))
    oxygen = calculate(
        bytes, max, lambda bit, x, _, count_of_one: bit == str(int(x == count_of_one))
    )
    co2 = calculate(
        bytes, min, lambda bit, x, count_of_zero, _: bit == str(int(x != count_of_zero))
    )
    print(oxygen * co2)
