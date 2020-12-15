#!/usr/bin/env python
from typing import Sequence

from aoc2020.input import get_puzzle_input


class Seats:
    def __init__(self, grid: Sequence[str]) -> None:
        chars = {"L", "#"}
        h, w = 0, 0
        self._hashmap = {}
        for i, row in enumerate(grid):
            for j, s in enumerate(row):
                if s in chars:
                    self._hashmap[complex(i, j)] = s
                    h, w = max(h, i), max(w, j)
        self._dim = (h + 1, w + 1)
        self._adj = (-1 - 1j, -1 + 0j, -1 + 1j, -1j, 1j, 1 - 1j, 1 + 0j, 1 + 1j)
        self._update_counter = 0

    def get_next_state(self, key: complex) -> str:
        current_status = self._hashmap[key]
        occupied_count = 0
        for offset in self._adj:
            occupied_count += self._hashmap.get(key + offset) == "#"
        if current_status == "L" and occupied_count == 0:
            self._update_counter += 1
            return "#"
        if current_status == "#" and occupied_count >= 4:
            self._update_counter += 1
            return "L"
        return current_status

    def update(self) -> int:
        self._update_counter = 0
        self._hashmap = {key: self.get_next_state(key) for key in self._hashmap}
        return self._update_counter

    def stabilize(self) -> int:
        while True:
            if self.update() == 0:
                return self.count_occupied()

    def count_occupied(self) -> int:
        return sum(s == "#" for s in self._hashmap.values())

    def to_grid(self):
        height, width = self._dim
        grid = [["." for _ in range(width)] for _ in range(height)]
        for k, v in self._hashmap.items():
            grid[int(k.real)][int(k.imag)] = v
        return grid

    def __str__(self) -> str:
        return "\n".join("".join(r) for r in self.to_grid())


def solve_first_part(puzzle_input: Sequence[str]) -> int:
    return Seats(puzzle_input).stabilize()


def solve_second_part(puzzle_input: Sequence[str]) -> int:
    return -1


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("day11")
    print(solve_first_part(puzzle_input))
    print(solve_second_part(puzzle_input))
