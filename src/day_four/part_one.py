#!/usr/bin/env python3
from functools import reduce


def calculate_score(drawn_numbers, bingo_card):
    last_drawn_number = drawn_numbers[-1]
    sum_of_undrawn_numbers = reduce(
        lambda a, row: a + sum(filter(lambda x: x not in drawn_numbers, row)),
        bingo_card,
        0,
    )
    return sum_of_undrawn_numbers * last_drawn_number


def is_winning(drawn_numbers, bingo_card):
    horizontally_winning = any(
        map(lambda x: all([n in drawn_numbers for n in x]), bingo_card)
    )
    vertically_winning = any(
        map(
            lambda x: all([row[x] in drawn_numbers for row in bingo_card]),
            range(len(bingo_card[0])),
        )
    )
    return horizontally_winning or vertically_winning


with open("input.txt") as input:
    drawn_numbers = list(map(lambda x: int(x), input.readline().strip().split(",")))
    bingo_card_lines = list(
        map(
            lambda x: [int(y) for y in x.split(" ") if y],
            filter(lambda x: x, map(lambda x: x.strip(), input.readlines())),
        )
    )
    bingo_cards = [
        bingo_card_lines[i : i + 5] for i in range(0, len(bingo_card_lines), 5)
    ]

    score = None
    for number_index in range(len(drawn_numbers)):
        for card_index, bingo_card in enumerate(bingo_cards):
            if is_winning(drawn_numbers[:number_index], bingo_card):
                score = calculate_score(drawn_numbers[:number_index], bingo_card)
                break
        if score is not None:
            break

    print(score)
