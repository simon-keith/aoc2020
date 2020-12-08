from typing import Sequence

from aoc2020.puzzle.day5 import parse_puzzle_input
from pytest import fixture


@fixture
def puzzle_input() -> Sequence[str]:
    return ("FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL")


def test_parsing(puzzle_input):
    assert parse_puzzle_input(puzzle_input) == (357, 567, 119, 820)