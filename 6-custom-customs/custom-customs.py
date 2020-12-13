from pathlib import Path
import operator
from functools import reduce

groups = []

with Path(__file__).parent.joinpath("data.txt").open() as f:
    for group in f.read().split("\n\n"):
        groups.append(group.strip().split("\n"))

print(1, sum([len(set("".join(group))) for group in groups]))

all_groups_yes = 0
for group in groups:
    everyone_yes = reduce(operator.and_, [set(u) for u in group])
    all_groups_yes += len(everyone_yes)

print(2, all_groups_yes)
