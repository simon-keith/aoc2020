#!/usr/bin/env python
import math
from typing import Sequence, Tuple

from aoc2020.input import get_puzzle_input
from aoc2020.puzzle import print_puzzle


class Ship:
    _direction = {"N": 1j, "S": -1j, "E": 1 + 0j, "W": -1 + 0j}
    _turn = {"L": 1, "R": -1}
    _forward = "F"

    def __init__(
        self,
        coodinates: complex = 0j,
        direction: complex = _direction["E"],
    ) -> None:
        self.coordinates = coodinates
        self.direction = direction

    def move(self, distance: int, direction: complex):
        self.coordinates += direction * distance

    def forward(self, distance: int):
        self.move(distance, self.direction)

    def execute(self, action: str, value: int):
        if (direction := self._direction.get(action)) is not None:
            self.move(value, direction)
        elif (turn := self._turn.get(action)) is not None:
            radians = math.radians(value * turn)
            self.direction *= complex(math.cos(radians), math.sin(radians))
        elif action == self._forward:
            self.forward(value)
        else:
            raise ValueError(f"unknown action '{action}'")


def parse_puzzle_input(puzzle_input: Sequence[str]) -> Sequence[Tuple[str, int]]:
    return tuple((s[0], int(s[1:])) for s in puzzle_input)


def solve_first_part(puzzle_input: Sequence[str]) -> int:
    intructions = parse_puzzle_input(puzzle_input)
    ship = Ship()
    for action, value in intructions:
        ship.execute(action, value)
    di, dj = math.fabs(ship.coordinates.real), math.fabs(ship.coordinates.imag)
    return round(di) + round(dj)


def solve_second_part(puzzle_input: Sequence[str]) -> int:
    return -1


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("day12")
    print_puzzle(puzzle_input, solve_first_part, solve_second_part)
