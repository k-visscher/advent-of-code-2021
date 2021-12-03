#!/usr/bin/env python3
gamma_rate = 0
epsilon_rate = 0

with open("input.txt") as f:
    bytes = list(map(lambda x: x.strip(), f.readlines()))
    for i in range(0, len(bytes[0])):
        count_of_zero = 0
        count_of_one = 0
        for byte in bytes:
            count_of_zero += list(byte)[i] == "0"
            count_of_one += list(byte)[i] == "1"
        if count_of_zero > count_of_one:
            gamma_rate = (gamma_rate << 1) | 1
            epsilon_rate = (epsilon_rate << 1) | 0
        else:
            gamma_rate = (gamma_rate << 1) | 0
            epsilon_rate = (epsilon_rate << 1) | 1

print(gamma_rate * epsilon_rate)
