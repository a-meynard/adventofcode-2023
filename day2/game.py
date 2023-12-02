from dataclasses import dataclass
from abc import ABC, abstractmethod

from revealed_set import RevealedSet


@dataclass(kw_only=True)
class Game:
    id: int
    revealed_sets: list[RevealedSet]


class GameProvider(ABC):
    @abstractmethod
    def get_all() -> list[Game]:
        pass
