import re

from category import Category


class IngestAlmanac:
    def __init__(self) -> None:
        self.categories: list[Category] = []
        self.initial_seeds: list[int] = []

    def source_destination_couple(self, source_start, destination_start, length):
        return zip(
            range(source_start, source_start + length),
            range(destination_start, destination_start + length),
        )

    def ingest_categories(self, input: list[str]):
        for line in input:
            if line == "":
                break

            m = re.search(r"(\w+)-to-(\w+) map:", line)
            if m is not None:
                current_source_category = m.group(1)
                current_destination_category = m.group(2)
            else:
                m = re.search(r"(\d+) (\d+) (\d+)", line)
                destination_start = int(m.group(1))
                source_start = int(m.group(2))
                range_length = int(m.group(3))
                for source, destination in self.source_destination_couple(
                    source_start, destination_start, range_length
                ):
                    self.categories.append(
                        Category(
                            name=current_source_category,
                            number=source,
                            destination_numer=destination,
                        )
                    )

    def ingest_initial_seeds(self, input: list[str]):
        all_numbers = re.search(r"^seeds: ((\d ?)+)", input)
        for seed in all_numbers.group(1).split(" "):
            self.initial_seeds.append(int(seed))

    def ingest(self, input: list[str]):
        self.ingest_initial_seeds(input=input[0])
        self.ingest_categories(input=input[2:])
