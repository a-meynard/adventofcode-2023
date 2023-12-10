import re

from category import Category, CategoryV2
from almanac import Almanac
from range_seed import RangeSeed
from feature_router import FeatureRouter


class IngestAlmanac:
    def __init__(self) -> None:
        self.categories: list[Category] = []
        if FeatureRouter.ENABLE_RANGE_SEED:
            self.initial_seeds: list[RangeSeed] = []
        else:
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
                continue

            m = re.search(r"(\w+)-to-(\w+) map:", line)
            if m is not None:
                current_source_category = m.group(1)
            else:
                m = re.search(r"(\d+) (\d+) (\d+)", line)
                destination_start = int(m.group(1))
                source_start = int(m.group(2))
                range_length = int(m.group(3))
                if FeatureRouter.ENABLE_CATEGORY_V2:
                    almanac.categories.append(
                        CategoryV2(
                            name=current_source_category,
                            source_start=source_start,
                            destination_start=destination_start,
                            range_length=range_length,
                        )
                    )
                else:
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
    def ingest_initial_seeds_with_ranges(almanac: Almanac, input: list[str]):
        all_numbers = [
            int(n) for n in re.search(r"^seeds: ((\d ?)+)", input).group(1).split(" ")
        ]
        for start, _range in zip(all_numbers[::2], all_numbers[1::2]):
            almanac.initial_seeds.append(RangeSeed(start=start, end=start + _range))

    @staticmethod
    def ingest_initial_seeds(almanac: Almanac, input: list[str]):
        all_numbers = re.search(r"^seeds: ((\d ?)+)", input)
        for seed in all_numbers.group(1).split(" "):
            almanac.initial_seeds.append(int(seed))

    def ingest(self, input: list[str]) -> Almanac:
        almanac = Almanac()
        print("ingest seeds")
        if FeatureRouter.ENABLE_RANGE_SEED:
            IngestAlmanac.ingest_initial_seeds_with_ranges(
                almanac=almanac, input=input[0]
            )
        else:
            IngestAlmanac.ingest_initial_seeds(almanac=almanac, input=input[0])
        print("ingest categories")
        IngestAlmanac.ingest_categories(almanac=almanac, input=input[2:])
        return almanac
