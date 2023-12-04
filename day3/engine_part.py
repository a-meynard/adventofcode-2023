from dataclasses import dataclass

from position import Position


@dataclass(frozen=True, kw_only=True)
class EnginePart:
    # NOTE: These are the 'symbol' object of the problem. We name them differently
    # because python already has a library called 'symbol' that we don't want
    # to override.
    position: Position

    def __post_init__(self):
        if self.position.start != self.position.end:
            raise ValueError(
                f"Part engines' position should be a point and not a line, got {self.position.start} and {self.position.end} as start and end position"
            )
