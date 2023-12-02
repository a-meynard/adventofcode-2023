from dataclasses import dataclass

from revealed_set import RevealedSet


@dataclass(kw_only=True)
class Game:
    id: int
    revealed_sets: list[RevealedSet]
