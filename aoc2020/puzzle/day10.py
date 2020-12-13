#!/usr/bin/env python
from itertools import chain
from typing import Dict, Sequence

from aoc2020.input import get_puzzle_input


def parse_puzzle_input(puzzle_input: Sequence[str]) -> Sequence[int]:
    adapters = [int(x) for x in puzzle_input]
    adapters.sort()
    return tuple(chain(adapters, [adapters[-1] + 3]))


def count_differences(adapters: Sequence[int]) -> Dict[int, int]:
    counter = {1: 0, 2: 0, 3: 0}
    rating = 0
    for a in adapters:
        counter[a - rating] += 1
        rating = a
    return counter


def count_arrangements(adapters: Sequence[int]) -> int:
    diffs = [1, 2, 3]
    counter = {0: 1}
    for a in adapters:
        counter[a] = sum(map(lambda i: counter.get(a - i, 0), diffs))
    return counter[adapters[-1]]


def solve_first_part(puzzle_input: Sequence[str]) -> int:
    adapters = parse_puzzle_input(puzzle_input)
    counter = count_differences(adapters)
    return counter[1] * counter[3]


def solve_second_part(puzzle_input: Sequence[str]) -> int:
    adapters = parse_puzzle_input(puzzle_input)
    return count_arrangements(adapters)


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("day10")
    print(solve_first_part(puzzle_input))
    print(solve_second_part(puzzle_input))
