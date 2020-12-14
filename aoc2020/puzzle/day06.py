#!/usr/bin/env python
from collections import Counter
from itertools import chain, groupby
from typing import Sequence

from aoc2020.input import get_puzzle_input


def parse_puzzle_input(puzzle_input: Sequence[str]) -> Sequence[Sequence[str]]:
    return tuple(tuple(v) for k, v in groupby(puzzle_input, lambda x: len(x) > 0) if k)


def count_any(answers: Sequence[str]) -> int:
    return len(set(chain.from_iterable(answers)))


def count_all(answers: Sequence[str]) -> int:
    group_size = len(answers)
    counter = Counter(chain.from_iterable(answers))
    return sum(c == group_size for c in counter.values())


def solve_first_part(puzzle_input: Sequence[str]) -> int:
    answers_list = parse_puzzle_input(puzzle_input)
    return sum(count_any(a) for a in answers_list)


def solve_second_part(puzzle_input: Sequence[str]) -> int:
    answers_list = parse_puzzle_input(puzzle_input)
    return sum(count_all(a) for a in answers_list)


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("day06")
    print(solve_first_part(puzzle_input))
    print(solve_second_part(puzzle_input))
