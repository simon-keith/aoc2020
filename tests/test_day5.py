from typing import Sequence

from aoc2020.puzzle.day5 import solve_first_part, solve_second_part
from pytest import fixture


@fixture
def puzzle_input() -> Sequence[str]:
    return ()


def test_first_part(puzzle_input):
    assert solve_first_part(puzzle_input) == 0


def test_second_part(puzzle_input):
    assert solve_second_part(puzzle_input) == 0
