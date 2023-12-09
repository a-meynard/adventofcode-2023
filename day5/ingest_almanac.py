import re

from category import Category
from almanac import Almanac


class IngestAlmanac:
    def __init__(self) -> None:
        self.categories: list[Category] = []
        self.initial_seeds: list[int] = []

    @staticmethod
    def source_destination_couple(source_start, destination_start, length):
        return zip(
            range(source_start, source_start + length),
            range(destination_start, destination_start + length),
        )

    @staticmethod
    def ingest_categories(almanac: Almanac, input: list[str]):
        for line in input:
            if line == "":
                break

            m = re.search(r"(\w+)-to-(\w+) map:", line)
            if m is not None:
                current_source_category = m.group(1)
            else:
                m = re.search(r"(\d+) (\d+) (\d+)", line)
                destination_start = int(m.group(1))
                source_start = int(m.group(2))
                range_length = int(m.group(3))
                for source, destination in IngestAlmanac.source_destination_couple(
                    source_start, destination_start, range_length
                ):
                    almanac.categories.append(
                        Category(
                            name=current_source_category,
                            number=source,
                            destination_numer=destination,
                        )
                    )

    @staticmethod
    def ingest_initial_seeds(almanac: Almanac, input: list[str]):
        all_numbers = re.search(r"^seeds: ((\d ?)+)", input)
        for seed in all_numbers.group(1).split(" "):
            almanac.initial_seeds.append(int(seed))

    def ingest(self, input: list[str]) -> Almanac:
        almanac = Almanac()
        IngestAlmanac.ingest_initial_seeds(almanac=almanac, input=input[0])
        IngestAlmanac.ingest_categories(almanac=almanac, input=input[2:])
        return almanac
