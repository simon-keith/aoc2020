#!/usr/bin/env python
from typing import Sequence, Tuple

from aoc2020.input import get_puzzle_input

SEAT_FRONT = {"F": True, "B": False}
SEAT_LEFT = {"L": True, "R": False}


def parse_puzzle_input(puzzle_input: Sequence[str]) -> Sequence[Tuple[str, str]]:
    return tuple((p[:7], p[7:]) for p in puzzle_input)


def split_range(r: range) -> Tuple[range, range]:
    range_length = len(r)
    if range_length < 2 or range_length % 2 != 0:
        raise ValueError(f"{r} is not splittable")
    diff = r.stop - r.start
    split_point = r.start + int(diff / 2)
    return range(r.start, split_point, r.step), range(split_point, r.stop, r.step)


def walk_directions(directions: Sequence[bool]) -> int:
    r = range(2 ** len(directions))
    for d in directions:
        if d:
            r, _ = split_range(r)
        else:
            _, r = split_range(r)
    return next(iter(r))


def decode_seat(rows: str, columns: str) -> Tuple[int, int]:
    row = walk_directions([SEAT_FRONT[r] for r in rows])
    column = walk_directions([SEAT_LEFT[c] for c in columns])
    return row, column


def get_seat_id(row: int, column: int) -> int:
    return row * 8 + column


def solve_first_part(puzzle_input: Sequence[str]) -> int:
    seat_list = parse_puzzle_input(puzzle_input)
    return max(get_seat_id(r, c) for r, c in (decode_seat(r, c) for r, c in seat_list))


def solve_second_part(puzzle_input: Sequence[str]) -> int:
    seat_list = parse_puzzle_input(puzzle_input)
    seat_id_set = set(
        get_seat_id(r, c) for r, c in (decode_seat(r, c) for r, c in seat_list)
    )
    for seat_id in range(min(seat_id_set), max(seat_id_set) + 1):
        if (
            seat_id not in seat_id_set
            and seat_id + 1 in seat_id_set
            and seat_id - 1 in seat_id_set
        ):
            return seat_id
    raise ValueError("could not find the seat id")


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("day5")
    print(solve_first_part(puzzle_input))
    print(solve_second_part(puzzle_input))
