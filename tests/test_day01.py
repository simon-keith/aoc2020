from typing import Sequence

from aoc2020.puzzle.day01 import solve_first_part, solve_second_part
from pytest import fixture


@fixture
def puzzle_input() -> Sequence[str]:
    return ("1721", "979", "366", "299", "675", "1456")


def test_first_part(puzzle_input):
    assert solve_first_part(puzzle_input) == 514579


def test_second_part(puzzle_input):
    assert solve_second_part(puzzle_input) == 241861950
