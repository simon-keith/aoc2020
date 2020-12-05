#!/usr/bin/env python
import re
from dataclasses import dataclass, fields
from itertools import chain, groupby
from typing import Dict, Optional, Sequence

from aoc2020.input import get_puzzle_input


def validate_int_value(value: str, min_value: int, max_value: int):
    try:
        int_value = int(value)
    except ValueError:
        return False
    return min_value <= int_value <= max_value


@dataclass
class Passeport:
    _HGT_PATTERN = re.compile(r"^(\d+)(\w{2})$")
    _HGT_RULES = {"in": (59, 76), "cm": (150, 193)}
    _HCL_PATTERN = re.compile(r"^(#[0-9a-f]{6})$")
    _ECL_SET = frozenset(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
    _PID_PATTERN = re.compile(r"^(\d{9})$")

    @classmethod
    def validate_byr(cls, v: str) -> str:
        assert validate_int_value(v, 1920, 2002)
        return v

    @classmethod
    def validate_iyr(cls, v: str) -> str:
        assert validate_int_value(v, 2010, 2020)
        return v

    @classmethod
    def validate_eyr(cls, v: str) -> str:
        assert validate_int_value(v, 2020, 2030)
        return v

    @classmethod
    def validate_hgt(cls, v: str) -> str:
        match = cls._HGT_PATTERN.match(v)
        assert match is not None
        value, unit = match.groups()
        assert unit in cls._HGT_RULES
        min_value, max_value = cls._HGT_RULES[unit]
        assert validate_int_value(value, min_value, max_value)
        return v

    @classmethod
    def validate_hcl(cls, v: str) -> str:
        assert cls._HCL_PATTERN.match(v) is not None
        return v

    @classmethod
    def validate_ecl(cls, v: str) -> str:
        assert v in cls._ECL_SET
        return v

    @classmethod
    def validate_pid(cls, v: str) -> str:
        assert cls._PID_PATTERN.match(v) is not None
        return v

    @classmethod
    def validate_cid(cls, v: Optional[str]) -> Optional[str]:
        return v

    byr: str  # (Birth Year)
    iyr: str  # (Issue Year)
    eyr: str  # (Expiration Year)
    hgt: str  # (Height)
    hcl: str  # (Hair Color)
    ecl: str  # (Eye Color)
    pid: str  # (Passport ID)
    cid: Optional[str] = None  # (Country ID)

    def __post_init__(self):
        self.byr = self.validate_byr(self.byr)
        self.iyr = self.validate_iyr(self.iyr)
        self.eyr = self.validate_eyr(self.eyr)
        self.hgt = self.validate_hgt(self.hgt)
        self.hcl = self.validate_hcl(self.hcl)
        self.ecl = self.validate_ecl(self.ecl)
        self.pid = self.validate_pid(self.pid)
        self.cid = self.validate_cid(self.cid)


def parse_puzzle_input(puzzle_input: Sequence[str]) -> Sequence[Dict[str, str]]:
    return tuple(
        dict(
            field.split(":")
            for field in chain.from_iterable(line.split() for line in v)
        )
        for k, v in groupby(puzzle_input, lambda x: len(x) > 0)
        if k
    )


def solve_first_part(puzzle_input: Sequence[str]) -> int:
    passeports = parse_puzzle_input(puzzle_input)
    expected_fields = set(f.name for f in fields(Passeport)) - {"cid"}
    return sum(expected_fields <= p.keys() for p in passeports)


def solve_second_part(puzzle_input: Sequence[str]) -> int:
    passeports = parse_puzzle_input(puzzle_input)
    valid_count = 0
    for kwargs in passeports:
        try:
            Passeport(**kwargs)
        except (TypeError, AssertionError):
            pass
        else:
            valid_count += 1
    return valid_count


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("day4")
    print(solve_first_part(puzzle_input))
    print(solve_second_part(puzzle_input))
