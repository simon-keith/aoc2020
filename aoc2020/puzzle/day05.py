#!/usr/bin/env python
from typing import Sequence

from aoc2020.input import get_puzzle_input

PUZZLE_MAPPING = {"F": "0", "B": "1", "L": "0", "R": "1"}


def parse_puzzle_input(puzzle_input: Sequence[str]) -> Sequence[int]:
    return tuple(int("".join(PUZZLE_MAPPING[c] for c in p), 2) for p in puzzle_input)


def solve_first_part(puzzle_input: Sequence[str]) -> int:
    return max(parse_puzzle_input(puzzle_input))


def solve_second_part(puzzle_input: Sequence[str]) -> int:
    seat_id_set = set(parse_puzzle_input(puzzle_input))
    for seat_id in range(min(seat_id_set) + 1, max(seat_id_set)):
        if (
            seat_id not in seat_id_set
            and seat_id + 1 in seat_id_set
            and seat_id - 1 in seat_id_set
        ):
            return seat_id
    raise ValueError("could not find the seat id")


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("day05")
    print(solve_first_part(puzzle_input))
    print(solve_second_part(puzzle_input))
