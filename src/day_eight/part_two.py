#!/usr/bin/env python3
from fluentpy import _
from collections import namedtuple

SignalPatternsAndOutputs = namedtuple(
    "SignalPatternsAndOutputs", ["signal_patterns", "outputs"]
)

num_to_seg_cnt = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}

with open("input.txt") as input:
    signals_and_outputs = (
        _(input.readlines())
        .map(
            lambda x: SignalPatternsAndOutputs(
                *_(x.split("|")).map(lambda y: y.strip().split(" ")).to(list)
            )
        )
        .to(list)
    )

    output_values = []

    for x in signals_and_outputs:
        segment_mapping = {
            "a": None,
            "b": None,
            "c": None,
            "d": None,
            "e": None,
            "f": None,
            "g": None,
        }
        numbers = [None] * 10

        numbers[1] = list(
            filter(lambda y: len(y) == num_to_seg_cnt[1], x.signal_patterns)
        )[0]
        numbers[4] = list(
            filter(lambda y: len(y) == num_to_seg_cnt[4], x.signal_patterns)
        )[0]
        numbers[7] = list(
            filter(lambda y: len(y) == num_to_seg_cnt[7], x.signal_patterns)
        )[0]
        numbers[8] = list(
            filter(lambda y: len(y) == num_to_seg_cnt[8], x.signal_patterns)
        )[0]

        segment_mapping["a"] = list(filter(lambda y: y not in numbers[1], numbers[7]))[
            0
        ]

        found = False
        for y in _(x.signal_patterns).filter(lambda y: len(y) == 6)._:
            for z in list(numbers[1]):
                if z not in y:
                    numbers[6] = y
                    segment_mapping["c"] = z
                    segment_mapping["f"] = numbers[1].replace(z, "")
                    found = True
                    break
            if found:
                break

        found = False
        for y in (
            _(x.signal_patterns).filter(lambda y: len(y) == 6 and y != numbers[6])._
        ):
            for z in list(numbers[4]):
                if z not in y:
                    numbers[0] = y
                    segment_mapping["d"] = z
                    found = True
                    break
            if found:
                break

        numbers[9] = (
            _(x.signal_patterns)
            .filter(lambda y: len(y) == 6 and y != numbers[6] and y != numbers[0])
            ._[0]
        )
        segment_mapping["e"] = list(set(numbers[8]).difference(set(numbers[9])))[0]
        numbers[5] = (
            _(x.signal_patterns)
            .filter(lambda y: len(y) == 5 and segment_mapping["c"] not in list(y))
            ._[0]
        )
        segment_mapping["b"] = list(
            set(numbers[8]).difference(
                set(
                    _(x.signal_patterns)
                    .filter(lambda y: len(y) == 5 and y != numbers[5])
                    ._[0]
                    + segment_mapping["f"]
                    + segment_mapping["e"]
                )
            )
        )[0]
        segment_mapping["g"] = list(
            set(numbers[8]).difference(
                set(numbers[4] + segment_mapping["a"] + segment_mapping["e"])
            )
        )[0]

        numbers[2] = (
            segment_mapping["a"]
            + segment_mapping["c"]
            + segment_mapping["d"]
            + segment_mapping["e"]
            + segment_mapping["g"]
        )
        numbers[3] = (
            segment_mapping["a"]
            + segment_mapping["c"]
            + segment_mapping["d"]
            + segment_mapping["f"]
            + segment_mapping["g"]
        )

        output = (
            _(x.outputs)
            .map(
                lambda y: _(enumerate(numbers)).filter(
                    lambda n: len(set(y).symmetric_difference(set(n[1]))) == 0
                )._
            )
            .map(lambda y: y[0][0])
            ._
        )
        output_values.append(int("".join(_(output).map(lambda y: str(y)))))

    print(sum(output_values))
