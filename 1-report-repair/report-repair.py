from itertools import product
from math import prod

from pathlib import Path

with Path(__file__).parent.joinpath("data.txt").open() as f:
    data = list(map(int, f.readlines()))

for repeat in [2, 3]:
    for vals in product(data, repeat=repeat):
        if sum(vals) == 2020:
            print(repeat, prod(vals))
            break
