#!/usr/bin/env python
from typing import Dict, Iterable, List, Sequence

from aoc2020.input import get_puzzle_input
from aoc2020.puzzle import print_puzzle


class Seat:
    def __init__(self, occupied: bool) -> None:
        self.occupied = occupied
        self._neighbours: List["Seat"] = []
        self._next_state = self.occupied

    def set_next_state(self, occupied: bool):
        self._next_state = occupied

    def update_state(self) -> bool:
        updated = self.occupied != self._next_state
        self.occupied = self._next_state
        return updated

    def set_neighbours(self, neighbours: Iterable["Seat"]):
        self._neighbours = list(neighbours)

    def count_occupied_neighbours(self) -> int:
        return sum(s.occupied for s in self._neighbours)


class SeatGrid:
    _adj = (-1 - 1j, -1 + 0j, -1 + 1j, -1j, 1j, 1 - 1j, 1 + 0j, 1 + 1j)
    _occupied_char = "#"
    _chars = frozenset([_occupied_char, "L"])

    def __init__(self, grid: Sequence[str], tolerance: int, observable: bool) -> None:
        self.tolerance = tolerance
        # initialize sparse matrix
        max_i, max_j = 0, 0
        self._sparse_grid: Dict[complex, Seat] = {}
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c in self._chars:
                    self._sparse_grid[complex(i, j)] = Seat(
                        occupied=c == self._occupied_char
                    )
                    max_i, max_j = max(max_i, i), max(max_j, j)
        self._dim = range(max_i + 1), range(max_j + 1)
        # initialize neighbours
        iter_func = self.iter_observable if observable else self.iter_adjacent
        for coordinates, seat in self._sparse_grid.items():
            seat.set_neighbours(iter_func(coordinates))

    def iter_adjacent(self, coordinates: complex) -> Iterable[Seat]:
        for direction in self._adj:
            seat = self._sparse_grid.get(coordinates + direction)
            if seat:
                yield seat

    def iter_observable(self, coordinates: complex) -> Iterable[Seat]:
        range_i, range_j = self._dim
        for direction in self._adj:
            key = coordinates + direction
            while key.real in range_i and key.imag in range_j:
                seat = self._sparse_grid.get(key)
                if seat:
                    yield seat
                    break
                key += direction

    def update_seats(self) -> int:
        for seat in self._sparse_grid.values():
            occupied_count = seat.count_occupied_neighbours()
            if not seat.occupied and occupied_count == 0:
                seat.set_next_state(True)
            elif seat.occupied and occupied_count >= self.tolerance:
                seat.set_next_state(False)
        update_counter = 0
        for seat in self._sparse_grid.values():
            update_counter += seat.update_state()
        return update_counter

    def count_occupied_seats(self) -> int:
        return sum(s.occupied for s in self._sparse_grid.values())

    def stabilize(self) -> int:
        while True:
            if self.update_seats() == 0:
                return self.count_occupied_seats()

    def to_grid(self):
        range_i, range_j = self._dim
        grid = [["." for _ in range_i] for _ in range_j]
        for k, v in self._sparse_grid.items():
            grid[int(k.real)][int(k.imag)] = v
        return grid

    def __str__(self) -> str:
        return "\n".join("".join(r) for r in self.to_grid())


def solve_first_part(puzzle_input: Sequence[str]) -> int:
    return SeatGrid(puzzle_input, 4, False).stabilize()


def solve_second_part(puzzle_input: Sequence[str]) -> int:
    return SeatGrid(puzzle_input, 5, True).stabilize()


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("day11")
    print_puzzle(puzzle_input, solve_first_part, solve_second_part)
