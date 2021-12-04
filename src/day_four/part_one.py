#!/usr/bin/env python3


def calculate_score_of_bingo_card(drawn_numbers, bingo_card):
    last_drawn_number = drawn_numbers[-1]
    sum_of_undrawn_numbers = 0

    for row in bingo_card:
        sum_of_undrawn_numbers += sum(filter(lambda x: x not in drawn_numbers, row))

    return sum_of_undrawn_numbers * last_drawn_number


def is_winning_bingo_card(drawn_numbers, bingo_card):
    horizontally_winning = False
    vertically_winning = False

    for horizontal_line in bingo_card:
        all_numbers_are_drawn_numbers = True
        for number in horizontal_line:
            if number not in drawn_numbers:
                all_numbers_are_drawn_numbers = False
        if all_numbers_are_drawn_numbers:
            horizontally_winning = True

    for i in range(len(bingo_card[0])):
        for vertical_line in [[row[i] for row in bingo_card]]:
            all_numbers_are_drawn_numbers = True
            for number in vertical_line:
                if number not in drawn_numbers:
                    all_numbers_are_drawn_numbers = False
            if all_numbers_are_drawn_numbers:
                vertically_winning = True

    return horizontally_winning or vertically_winning


with open("input.txt") as input:
    drawn_numbers = list(map(lambda x: int(x), input.readline().strip().split(",")))

    raw_bingo_card_lines = filter(
        lambda x: x, map(lambda x: x.strip(), input.readlines())
    )
    parsed_bingo_card_lines = list(
        map(lambda x: [int(y) for y in x.split(" ") if y], raw_bingo_card_lines)
    )

    bingo_cards = [
        parsed_bingo_card_lines[i : i + 5]
        for i in range(0, len(parsed_bingo_card_lines), 5)
    ]

    score = None
    for number_index in range(len(drawn_numbers)):
        for card_index, bingo_card in enumerate(bingo_cards):
            if is_winning_bingo_card(drawn_numbers[:number_index], bingo_card):
                score = calculate_score_of_bingo_card(
                    drawn_numbers[:number_index], bingo_card
                )
                break
        if score is not None:
            break

    print(score)
