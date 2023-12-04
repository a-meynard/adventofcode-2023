from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class Position:
    start: int
    end: int
    line: int
