from scratchcard import ScratchCard


class ExpandScratchCards:
    def __init__(self) -> None:
        pass

    def handle(self, scratchcards: list[ScratchCard]) -> list[ScratchCard]:
        cards_by_id = {c.id: [c] for c in scratchcards}
        for id, _scratchcards in cards_by_id.items():
            for scratchcard in _scratchcards:
                for i in range(scratchcard.worth_value()):
                    cards_by_id[scratchcard.id + i + 1].append(
                        cards_by_id[scratchcard.id + i + 1][0]
                    )

        return [s for c in cards_by_id.values() for s in c]
