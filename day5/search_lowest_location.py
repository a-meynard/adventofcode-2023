from almanac import Almanac
from range_seed import RangeSeed


class SearchLowestLocation:
    def __init__(self) -> None:
        self.category_types = []

    def find_location(self, almanac: Almanac, seed: int | RangeSeed) -> int:
        next_stop = seed
        for category_type in almanac.category_types():
            next_stop = almanac.convert_number(
                category_type=category_type, number=next_stop
            )
        return next_stop

    def handle(self, almanac: Almanac) -> int:
        return min(
            [
                self.find_location(almanac=almanac, seed=seed)
                for seed in almanac.initial_seeds
            ]
        )

    def handle2(self, almanac: Almanac) -> int:
        lowest = 1000000
        while True:
            if lowest % 10000 == 0:
                print(lowest)
            if almanac.is_connected_to_a_seed(lowest):
                return lowest
            else:
                lowest += 1
