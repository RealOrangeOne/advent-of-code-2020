from pathlib import Path
import re
from dataclasses import dataclass

MATCHER = re.compile(r"^(\d+)\-(\d+) (\S+): (\S+?)$")


@dataclass()
class PasswordEntry:
    min_count: int
    max_count: int
    target_char: str
    password_candidate: str


def line_to_password_entry(line: str) -> PasswordEntry:
    match = MATCHER.match(line)
    return PasswordEntry(
        min_count=int(match.group(1)),
        max_count=int(match.group(2)),
        target_char=match.group(3),
        password_candidate=match.group(4),
    )


with Path(__file__).parent.joinpath("data.txt").open() as f:
    password_database = [line_to_password_entry(line) for line in f.readlines()]


valid_passwords = 0

for entry in password_database:
    occurances = entry.password_candidate.count(entry.target_char)
    if entry.min_count <= occurances <= entry.max_count:
        valid_passwords += 1

print("valid 1", valid_passwords)

valid_passwords = 0

for entry in password_database:
    min_match = entry.password_candidate[entry.min_count - 1] == entry.target_char
    max_match = entry.password_candidate[entry.max_count - 1] == entry.target_char
    if min_match ^ max_match:
        valid_passwords += 1

print("valid 2", valid_passwords)
