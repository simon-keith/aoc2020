from typing import Sequence

from aoc2020.puzzle.day12 import solve_first_part, solve_second_part
from pytest import fixture


@fixture
def puzzle_input() -> Sequence[str]:
    return ("F10", "N3", "F7", "R90", "F11")


def test_first_part(puzzle_input):
    assert solve_first_part(puzzle_input) == 25


def test_second_part(puzzle_input):
    assert solve_second_part(puzzle_input) == 0
