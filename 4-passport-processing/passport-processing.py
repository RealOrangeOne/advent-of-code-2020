from pathlib import Path
from enum import Enum
import re
from typing import List, Dict


class PassportField(Enum):
    BIRTH_YEAR = "byr"
    ISSUE_YEAR = "iyr"
    EXPIRATION_YEAR = "eyr"
    HEIGHT = "hgt"
    HAIR_COLOUR = "hcl"
    EYE_COLOUR = "ecl"
    PASSPORT_ID = "pid"
    COUNTRY_ID = "cid"


def parse_passport_data(line):
    passport = {}

    for passport_field in line.strip().split(" "):
        field, value = passport_field.split(":")
        passport[PassportField(field)] = value

    return passport


def validate(field: PassportField, value: str):
    if field == PassportField.BIRTH_YEAR:
        return 1920 <= int(value) <= 2002
    elif field == PassportField.ISSUE_YEAR:
        return 2010 <= int(value) <= 2020
    elif field == PassportField.EXPIRATION_YEAR:
        return 2020 <= int(value) <= 2030
    elif field == PassportField.HEIGHT:
        if value.endswith("cm"):
            return 150 <= int(value.rstrip("cm")) <= 193
        elif value.endswith("in"):
            return 59 <= int(value.rstrip("in")) <= 76
        return False
    elif field == PassportField.HAIR_COLOUR:
        return re.match(r"^#[0-9a-f]{6}$", value) is not None
    elif field == PassportField.EYE_COLOUR:
        return value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    elif field == PassportField.PASSPORT_ID:
        return re.match(r"^[0-9]{9}$", value) is not None
    else:
        return True


passports: List[Dict[PassportField, str]] = []

with Path(__file__).parent.joinpath("data.txt").open() as f:
    for passport_data in f.read().split("\n\n"):
        passports.append(parse_passport_data(passport_data.replace("\n", " ")))


valid_passports = []

for passport in passports:
    for field in PassportField:
        if field not in passport and field != PassportField.COUNTRY_ID:
            break
    else:
        valid_passports.append(passport)

print(1, len(valid_passports))

second_valid_passports = []

for passport in valid_passports:
    for field, value in passport.items():
        if not validate(field, value):
            break
    else:
        second_valid_passports.append(passport)

print(2, len(second_valid_passports))
