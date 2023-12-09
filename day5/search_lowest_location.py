from almanac import Almanac


class SearchLowestLocation:
    def __init__(self) -> None:
        self.category_types = []

    def find_location(self, almanac: Almanac, seed: int) -> int:
        next_stop = seed
        for category_type in self.category_types:
            for category in [c for c in almanac.categories if c.name == category_type]:
                if category.number == next_stop:
                    next_stop = category.destination_numer
                    break
        return next_stop

    def handle(self, almanac: Almanac) -> int:
        # HACK: Here we use the fact that the Almanac probably has its category
        # ordered in the correct way.
        self.category_types = []
        for category in almanac.categories:
            # NOTE: Could be optimized with an OrderedSet data type
            if category.name not in self.category_types:
                self.category_types.append(category.name)

        return min(
            [
                self.find_location(almanac=almanac, seed=seed)
                for seed in almanac.initial_seeds
            ]
        )
