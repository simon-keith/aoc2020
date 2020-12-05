from typing import Sequence

from aoc2020.puzzle.day5 import decode_seat, parse_puzzle_input, solve_first_part
from pytest import fixture


@fixture
def puzzle_input() -> Sequence[str]:
    return ("FBFBBFFRLR", "FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL")


def test_first_part(puzzle_input):
    seat_list = parse_puzzle_input(puzzle_input)
    decoded_seat_list = tuple(decode_seat(r, c) for r, c in seat_list)
    assert decoded_seat_list == ((44, 5), (44, 5), (70, 7), (14, 7), (102, 4))
    assert solve_first_part(puzzle_input) == 820
