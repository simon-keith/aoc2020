#!/usr/bin/env python
from typing import Iterable, Sequence, Set, Tuple

from aoc2020.input import get_puzzle_input
from aoc2020.puzzle import print_puzzle

PUZZLE_TARGET = 2020


def parse_puzzle_input(puzzle_input: Sequence[str]) -> Sequence[int]:
    return tuple(int(x) for x in puzzle_input)


def iter_pairs_that_sum_to_target(
    integer_set: Set[int], target: int
) -> Iterable[Tuple[int, int]]:
    for i in integer_set:
        diff = target - i
        if diff in integer_set:
            yield i, diff


def iter_triples_that_sum_to_target(
    integer_set: Set[int], target: int
) -> Iterable[Tuple[int, int]]:
    for i in integer_set:
        diff = target - i
        for pair in iter_pairs_that_sum_to_target(integer_set, diff):
            yield i, *pair


def solve_first_part(puzzle_input: Sequence[str]) -> int:
    integer_set = set(parse_puzzle_input(puzzle_input))
    try:
        a, b = next(iter_pairs_that_sum_to_target(integer_set, PUZZLE_TARGET))
    except StopIteration as e:
        raise ValueError(f"found no pair that sum to {PUZZLE_TARGET}") from e
    return a * b


def solve_second_part(puzzle_input: Sequence[str]) -> int:
    integer_set = set(parse_puzzle_input(puzzle_input))
    try:
        a, b, c = next(iter_triples_that_sum_to_target(integer_set, PUZZLE_TARGET))
    except StopIteration as e:
        raise ValueError(f"found no triple that sum to {PUZZLE_TARGET}") from e
    return a * b * c


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("day01")
    print_puzzle(puzzle_input, solve_first_part, solve_second_part)
