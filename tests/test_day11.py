from typing import Sequence

from aoc2020.puzzle.day11 import solve_first_part, solve_second_part
from pytest import fixture


@fixture
def puzzle_input() -> Sequence[str]:
    return (
        "L.LL.LL.LL",
        "LLLLLLL.LL",
        "L.L.L..L..",
        "LLLL.LL.LL",
        "L.LL.LL.LL",
        "L.LLLLL.LL",
        "..L.L.....",
        "LLLLLLLLLL",
        "L.LLLLLL.L",
        "L.LLLLL.LL",
    )


def test_first_part(puzzle_input):
    assert solve_first_part(puzzle_input) == 37


def test_second_part(puzzle_input):
    assert solve_second_part(puzzle_input) == 0
