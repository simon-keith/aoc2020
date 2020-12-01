from typing import Tuple

from aoc2020.puzzle.day1 import solve_first_puzzle
from pytest import fixture


@fixture
def puzzle_input() -> Tuple:
    return ("1721", "979", "366", "299", "675", "1456")


def test_first_puzzle(puzzle_input):
    assert solve_first_puzzle(puzzle_input) == 514579
