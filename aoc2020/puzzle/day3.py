#!/usr/bin/env python
import math
from typing import Sequence

from aoc2020.input import get_puzzle_input

PUZZLE_SLOPES = (
    (3, 1),
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
)


def count_trees_in_path(puzzle_input: Sequence[str], right: int, down: int) -> int:
    count = 0
    i, j = 0, 0
    while i < len(puzzle_input) - down:
        i += down
        row = puzzle_input[i]
        j = (j + right) % len(row)
        count += row[j] == "#"
    return count


def solve_first_part(puzzle_input: Sequence[str]) -> int:
    return count_trees_in_path(puzzle_input, *PUZZLE_SLOPES[0])


def solve_second_part(puzzle_input: Sequence[str]) -> int:
    return math.prod(
        count_trees_in_path(puzzle_input, right, down)
        for right, down in PUZZLE_SLOPES[1:]
    )


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("day3")
    print(solve_first_part(puzzle_input))
    print(solve_second_part(puzzle_input))
