from pathlib import Path
import re
from functools import lru_cache

REGEX = re.compile("(\w+ \w+) bags contain (.+).")
INNER_BAG_REGEX = re.compile("(\d+) (\w+ \w+) bags?")

TARGET_BAG = "shiny gold"

bags = {}

with Path(__file__).parent.joinpath("data.txt").open() as f:
    for line in f.readlines():
        bag_line = REGEX.match(line)
        bag = bag_line.group(1)
        inner_bag_text = bag_line.group(2)
        inner_bags = []
        for count, inner_bag in INNER_BAG_REGEX.findall(inner_bag_text):
            for _ in range(int(count)):
                inner_bags.append(inner_bag)
        bags[bag] = inner_bags


@lru_cache(maxsize=None)
def can_hold_target_bag(bag_name):
    inner_bags = bags[bag_name]
    if TARGET_BAG in inner_bags:
        return True
    for inner_bag in inner_bags:
        if can_hold_target_bag(inner_bag):
            return True
    return False


@lru_cache(maxsize=None)
def flatten_inner_bags(bag_name):
    inner_bags = bags[bag_name]
    all_inner_bags = inner_bags.copy()
    for inner_bag in inner_bags:
        all_inner_bags += flatten_inner_bags(inner_bag)
    return all_inner_bags


def main():

    bags_can_hold = set()
    for bag in bags.keys():
        if can_hold_target_bag(bag):
            bags_can_hold.add(bag)

    print(1, len(bags_can_hold))

    print(2, len(flatten_inner_bags(TARGET_BAG)))


if __name__ == "__main__":
    main()
