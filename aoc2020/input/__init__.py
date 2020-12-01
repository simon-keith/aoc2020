import functools
import pathlib
import typing

_here = pathlib.Path(__file__).parent.resolve()


def _read_file(path: pathlib.PosixPath):
    with path.open() as f:
        text = f.read()
    lines = tuple(text.splitlines())
    return lines


@functools.cache
def get_puzzle_input(name: str) -> typing.Tuple[str]:
    path = _here / f"{name}.txt"
    try:
        return _read_file(path=path)
    except FileNotFoundError:
        raise ValueError(f"no puzzle input for '{name}'")
