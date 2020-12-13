from typing import Sequence

from aoc2020.puzzle.day10 import solve_first_part, solve_second_part
from pytest import fixture


@fixture
def small_puzzle_input() -> Sequence[str]:
    return (
        "16",
        "10",
        "15",
        "5",
        "1",
        "11",
        "7",
        "19",
        "6",
        "12",
        "4",
    )


@fixture
def large_puzzle_input() -> Sequence[str]:
    return (
        "28",
        "33",
        "18",
        "42",
        "31",
        "14",
        "46",
        "20",
        "48",
        "47",
        "24",
        "23",
        "49",
        "45",
        "19",
        "38",
        "39",
        "11",
        "1",
        "32",
        "25",
        "35",
        "8",
        "17",
        "7",
        "9",
        "4",
        "2",
        "34",
        "10",
        "3",
    )


def test_first_part(small_puzzle_input, large_puzzle_input):
    assert solve_first_part(small_puzzle_input) == 7 * 5
    assert solve_first_part(large_puzzle_input) == 22 * 10


def test_second_part(small_puzzle_input, large_puzzle_input):
    assert solve_second_part(small_puzzle_input) == 0
