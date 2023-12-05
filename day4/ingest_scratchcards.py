import re

from scratchcard import ScratchCard


class IngestScratchCards:
    def __init__(self) -> None:
        pass

    @staticmethod
    def extract_card_id(raw_scratchcard: str) -> int:
        m = re.search(r"^Card\s+(\d+):", raw_scratchcard)
        return int(m.group(1))

    @staticmethod
    def extract_numbers(card_id: str, raw_scratchcard: str) -> (set[int], set[int]):
        raw_numbers = raw_scratchcard[raw_scratchcard.index(":") + 1 :]

        if raw_numbers.split(" | ") == [""]:
            return set(), set()

        raw_winning_numbers, numbers_you_have = raw_numbers.split(" | ")
        winning_numbers = {
            int(r) for r in list(filter(None, raw_winning_numbers.split(" ")))
        }
        numbers = {int(r) for r in list(filter(None, numbers_you_have.split(" ")))}

        return winning_numbers, numbers

    def handle(self, raw_scratchcards: list[str]) -> list[ScratchCard]:
        scratchcards: list[ScratchCard] = []
        for raw_scratchcard in raw_scratchcards:
            card_id = IngestScratchCards.extract_card_id(
                raw_scratchcard=raw_scratchcard
            )
            winning_numbers, numbers = IngestScratchCards.extract_numbers(
                card_id=card_id, raw_scratchcard=raw_scratchcard
            )
            scratchcards.append(
                ScratchCard(
                    id=card_id, winning_numbers=winning_numbers, numbers=numbers
                )
            )
        return scratchcards
