#!/usr/bin/env python
from typing import Sequence, Dict

from aoc2020.input import get_puzzle_input


def parse_puzzle_input(puzzle_input: Sequence[str]) -> Sequence[int]:
    return tuple(sorted(int(x) for x in puzzle_input))


def count_differences(adapters: Sequence[int]) -> Dict[int, int]:
    counter = {1: 0, 2: 0, 3: 1}
    rating = 0
    for a in adapters:
        counter[a - rating] += 1
        rating = a
    return counter


def count_arrangements(adapters: Sequence[int], i: int = 0) -> int:
    pass


def solve_first_part(puzzle_input: Sequence[str]) -> int:
    adapters = parse_puzzle_input(puzzle_input)
    counter = count_differences(adapters)
    return counter[1] * counter[3]


def solve_second_part(puzzle_input: Sequence[str]) -> int:
    return -1


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("day10")
    print(solve_first_part(puzzle_input))
    print(solve_second_part(puzzle_input))
