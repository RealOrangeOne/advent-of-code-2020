from pathlib import Path
from math import prod

trees = set()

with Path(__file__).parent.joinpath("data.txt").open() as f:
    for line_no, line in enumerate(f.readlines()):
        for col_no, char in enumerate(line):
            if char == "#":
                trees.add((col_no, line_no))
    max_col_no = col_no
    max_line_no = line_no


def count_trees(translation):
    current_pos = (0, 0)
    hit_trees = 0

    while True:
        if current_pos in trees:
            hit_trees += 1
        if current_pos[1] >= max_line_no:
            return hit_trees
        current_pos = (
            (current_pos[0] + translation[0]) % max_col_no,
            current_pos[1] + translation[1],
        )


print(1, count_trees((3, 1)))

print(
    2, prod([count_trees(slope) for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]])
)
