from pathlib import Path
from itertools import product, accumulate

CODES = []
WINDOW_SIZE = 25

with Path(__file__).parent.joinpath("data.txt").open() as f:
    for line in f.readlines():
        CODES.append(int(line))


def find_window_summing_to(target):
    for window_size in range(2, len(CODES)):
        for start in range(len(CODES) - window_size):
            window = CODES[start : start + window_size]
            if sum(window) == target:
                return window


for i in range(WINDOW_SIZE + 1, len(CODES[WINDOW_SIZE:])):
    code = CODES[i]
    previous = CODES[i - WINDOW_SIZE - 1 : i]
    valid_code = False
    for vals in product(previous, repeat=2):
        if sum(vals) == code:
            valid_code = True
            break

    if not valid_code:
        print(1, code)
        break

window = find_window_summing_to(code)

print(2, min(window) + max(window))
