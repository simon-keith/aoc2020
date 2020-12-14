#!/usr/bin/env python
from typing import Sequence

from aoc2020.input import get_puzzle_input
from aoc2020.puzzle.day01 import iter_pairs_that_sum_to_target

PUZZLE_PREAMBLE = 25


def parse_puzzle_input(puzzle_input: Sequence[str]) -> Sequence[int]:
    return tuple(int(p) for p in puzzle_input)


def find_weakness(integers: Sequence[int], preamble: int) -> int:
    reference = set(integers[:preamble])
    for i in range(preamble, len(integers)):
        target = integers[i]
        try:
            next(iter_pairs_that_sum_to_target(reference, target))
        except StopIteration:
            return target
        old, new = integers[i - preamble], integers[i]
        reference.remove(old)
        reference.add(new)
    raise ValueError("did not find any weakness")


def find_contiguous_tuple(integers: Sequence[int], target: int) -> Sequence[int]:
    lower, upper = 0, 2
    total = integers[lower] + integers[upper - 1]
    while upper <= len(integers):
        if total < target:
            total += integers[upper]
            upper += 1
        elif total > target:
            total -= integers[lower]
            lower += 1
        else:
            return tuple(integers[lower:upper])
    raise ValueError("did not find any continuous tuple")


def solve_first_part(
    puzzle_input: Sequence[str], preamble: int = PUZZLE_PREAMBLE
) -> int:
    integers = parse_puzzle_input(puzzle_input)
    return find_weakness(integers, preamble)


def solve_second_part(
    puzzle_input: Sequence[str], preamble: int = PUZZLE_PREAMBLE
) -> int:
    integers = parse_puzzle_input(puzzle_input)
    weakness = find_weakness(integers, preamble)
    contiguous_tuple = find_contiguous_tuple(integers, weakness)
    return min(contiguous_tuple) + max(contiguous_tuple)


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("day09")
    print(solve_first_part(puzzle_input))
    print(solve_second_part(puzzle_input))
