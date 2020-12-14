from typing import Sequence

from aoc2020.puzzle.day03 import (
    PUZZLE_SLOPES,
    count_trees_in_path,
    solve_first_part,
    solve_second_part,
)
from pytest import fixture


@fixture
def puzzle_input() -> Sequence[str]:
    return (
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#",
    )


def test_first_part(puzzle_input):
    assert solve_first_part(puzzle_input) == 7


def test_second_part(puzzle_input):
    assert tuple(
        count_trees_in_path(puzzle_input, right, down)
        for right, down in PUZZLE_SLOPES[1:]
    ) == (2, 7, 3, 4, 2)
    assert solve_second_part(puzzle_input) == 336
