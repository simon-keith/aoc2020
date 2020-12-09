from typing import Sequence

from aoc2020.puzzle.day9 import solve_first_part, solve_second_part
from pytest import fixture


@fixture
def puzzle_input() -> Sequence[str]:
    return (
        "35",
        "20",
        "15",
        "25",
        "47",
        "40",
        "62",
        "55",
        "65",
        "95",
        "102",
        "117",
        "150",
        "182",
        "127",
        "219",
        "299",
        "277",
        "309",
        "576",
    )


def test_first_part(puzzle_input):
    assert solve_first_part(puzzle_input, 5) == 127


def test_second_part(puzzle_input):
    assert solve_second_part(puzzle_input, 5) == 62
