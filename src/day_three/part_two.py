#!/usr/bin/env python3
oxygen_candidates = []
with open("input.txt") as f:
    bytes = list(map(lambda x: x.strip(), f.readlines()))

    oxygen_candidates = bytes
    co2_candidates = bytes

    for i in range(0, len(bytes[0])):
        oxygen_counts_of_zero = 0
        oxygen_counts_of_one = 0

        for byte in oxygen_candidates:
            if byte[i] == "1":
                oxygen_counts_of_one += 1
            elif byte[i] == "0":
                oxygen_counts_of_zero += 1

        most = max(oxygen_counts_of_zero, oxygen_counts_of_one)
        oxygen_candidates = [
            candidate
            for candidate in oxygen_candidates
            if candidate[i] == str(int(most == oxygen_counts_of_one))
        ]
        if len(oxygen_candidates) == 1:
            break

    for i in range(0, len(bytes[0])):
        co2_counts_of_zero = 0
        co2_counts_of_one = 0

        for byte in co2_candidates:
            if byte[i] == "1":
                co2_counts_of_one += 1
            elif byte[i] == "0":
                co2_counts_of_zero += 1

        least = min(co2_counts_of_zero, co2_counts_of_one)
        co2_candidates = [
            candidate
            for candidate in co2_candidates
            if candidate[i] != str(int(least == co2_counts_of_zero))
        ]
        if len(co2_candidates) == 1:
            break

print(int(oxygen_candidates[0], base=2) * int(co2_candidates[0], base=2))
