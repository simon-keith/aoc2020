#!/usr/bin/env python
from typing import Sequence

from aoc2020.input import get_puzzle_input
from aoc2020.puzzle import print_puzzle


def solve_first_part(puzzle_input: Sequence[str]) -> int:
    return -1


def solve_second_part(puzzle_input: Sequence[str]) -> int:
    return -1


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("day12")
    print_puzzle(puzzle_input, solve_first_part, solve_second_part)
