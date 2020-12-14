#!/usr/bin/env python
from itertools import chain
from typing import Sequence

from aoc2020.input import get_puzzle_input


class Seats:
    def __init__(self, grid: Sequence[str]) -> None:
        self.h = range(len(grid))
        self.w = range(len(grid[0])) if self.h else range(0)
        self.grid = [[grid[i][j] for j in self.w] for i in self.h]
        self._update_counter = 0

    def get_next_state(self, i: int, j: int) -> str:
        current_status = self.grid[i][j]
        if current_status == ".":
            return "."
        occupied_count = 0
        for m in range(i - 1, i + 2):
            for n in range(j - 1, j + 2):
                if m in self.h and n in self.w and (i, j) != (m, n):
                    occupied_count += self.grid[m][n] == "#"
        if current_status == "L" and occupied_count == 0:
            self._update_counter += 1
            return "#"
        if current_status == "#" and occupied_count >= 4:
            self._update_counter += 1
            return "L"
        return current_status

    def update(self) -> int:
        self._update_counter = 0
        self.grid = [[self.get_next_state(i, j) for j in self.w] for i in self.h]
        return self._update_counter

    def stabilize(self) -> int:
        while True:
            if self.update() == 0:
                return self.count_occupied()

    def count_occupied(self) -> int:
        return sum(chain.from_iterable((c == "#" for c in r) for r in self.grid))

    def __str__(self) -> str:
        return "\n".join("".join(r) for r in self.grid)


def solve_first_part(puzzle_input: Sequence[str]) -> int:
    return Seats(puzzle_input).stabilize()


def solve_second_part(puzzle_input: Sequence[str]) -> int:
    return -1


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("day11")
    print(solve_first_part(puzzle_input))
    print(solve_second_part(puzzle_input))
