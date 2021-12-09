#!/usr/bin/env python3
from fluentpy import _

with open("input.txt") as input:
    rows = (
        _(input.readlines())
        .map(lambda x: _(list(x.strip())).map(lambda y: int(y)).to(list))
        .to(list)
    )
