from statistics import mean
from math import floor, ceil

from pathlib import Path

with Path(__file__).parent.joinpath("data.txt").open() as f:
    boarding_passes = [l.strip() for l in f.readlines()]


def get_row(boarding_pass):
    ub = 127
    lb = 0
    for char in boarding_pass[:-4]:
        midpoint = mean([ub, lb])
        if char == "F":
            ub = floor(midpoint)
        elif char == "B":
            lb = ceil(midpoint)
    if boarding_pass[-4] == "F":
        return lb
    return ub


def get_column(boarding_pass):
    ub = 7
    lb = 0
    for char in boarding_pass[-3:-1]:
        midpoint = mean([ub, lb])
        if char == "L":
            ub = floor(midpoint)
        elif char == "R":
            lb = ceil(midpoint)
    if boarding_pass[-1] == "L":
        return lb
    return ub


def get_row_column(boarding_pass):
    return get_row(boarding_pass), get_column(boarding_pass)


def get_seat_id(row, col):
    return (row * 8) + col


assert get_row_column("FBFBBFFRLR") == (44, 5)
assert get_row_column("BFFFBBFRRR") == (70, 7)
assert get_row_column("FFFBBBFRRR") == (14, 7)
assert get_row_column("BBFFBBFRLL") == (102, 4)
assert get_seat_id(44, 5) == 357
assert get_seat_id(70, 7) == 567
assert get_seat_id(14, 7) == 119
assert get_seat_id(102, 4) == 820


def main():
    seat_ids = set()

    for boarding_pass in boarding_passes:
        row, col = get_row_column(boarding_pass.strip())
        seat_id = get_seat_id(row, col)
        seat_ids.add(seat_id)
    print(1, max(seat_ids))

    print(2, set(range(min(seat_ids), max(seat_ids))).difference(seat_ids).pop())


if __name__ == "__main__":
    main()
