#!/usr/bin/env python
from typing import Sequence

from aoc2020.input import get_puzzle_input


class Seats:
    _occupied = "#"
    _empty = "L"
    _chars = frozenset([_occupied, _empty])
    _adj = (-1 - 1j, -1 + 0j, -1 + 1j, -1j, 1j, 1 - 1j, 1 + 0j, 1 + 1j)

    def __init__(self, grid: Sequence[str], tolerance: int, observable: bool) -> None:
        self.tolerance = tolerance
        self.observable = observable
        h, w = 0, 0
        self._hashmap = {}
        for i, row in enumerate(grid):
            for j, s in enumerate(row):
                if s in self._chars:
                    self._hashmap[complex(i, j)] = s
                    h, w = max(h, i), max(w, j)
        self._dim = (range(h + 1), range(w + 1))
        self._update_counter = 0

    def count_occupied_neighbors(self, key: complex) -> int:
        occupied_count = 0
        for direction in self._adj:
            occupied_count += self._hashmap.get(key + direction) == self._occupied
        return occupied_count

    def count_occupied_observable(self, key: complex) -> int:
        occupied_count = 0
        for direction in self._adj:
            factor = 1
            while True:
                k = key + factor * direction
                if not (k.real in self._dim[0] and k.imag in self._dim[1]):
                    break
                seat = self._hashmap.get(k)
                if seat is not None:
                    occupied_count += seat == self._occupied
                    break
                factor += 1
        return occupied_count

    def get_next_state(self, key: complex) -> str:
        current_status = self._hashmap[key]
        occupied_count = (
            self.count_occupied_observable(key)
            if self.observable
            else self.count_occupied_neighbors(key)
        )
        if current_status == self._empty and occupied_count == 0:
            self._update_counter += 1
            return self._occupied
        if current_status == self._occupied and occupied_count >= self.tolerance:
            self._update_counter += 1
            return self._empty
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
        return sum(s == self._occupied for s in self._hashmap.values())

    def to_grid(self):
        height, width = self._dim
        grid = [["." for _ in width] for _ in height]
        for k, v in self._hashmap.items():
            grid[int(k.real)][int(k.imag)] = v
        return grid

    def __str__(self) -> str:
        return "\n".join("".join(r) for r in self.to_grid())


def solve_first_part(puzzle_input: Sequence[str]) -> int:
    return Seats(puzzle_input, 4, False).stabilize()


def solve_second_part(puzzle_input: Sequence[str]) -> int:
    return Seats(puzzle_input, 5, True).stabilize()


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("day11")
    print(solve_first_part(puzzle_input))
    print(solve_second_part(puzzle_input))
