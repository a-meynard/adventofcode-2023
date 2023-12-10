from dataclasses import dataclass, field

from category import Category, CategoryV2
from range_seed import RangeSeed


@dataclass
class Almanac:
    initial_seeds: list[int | RangeSeed] = field(default_factory=list)
    categories: list[Category | CategoryV2] = field(default_factory=list)

    def category_types(self):
        # HACK: Here we use the fact that the Almanac probably has its category
        # ordered in the correct way.
        category_types = []
        for category in self.categories:
            # NOTE: Could be optimized with an OrderedSet data type
            if category.name not in category_types:
                category_types.append(category.name)
        return category_types

    def convert_number(self, category_type: str, number: int):
        next_stop = number
        for category in [c for c in self.categories if c.name == category_type]:
            if category.get_to_destination(number=next_stop) != next_stop:
                next_stop = category.get_to_destination(number=next_stop)
                break
        return next_stop

    def go_to_source(self, category_type: str, number: int):
        next_stop = number
        for category in [c for c in self.categories if c.name == category_type]:
            if category.get_to_source(number=next_stop) != next_stop:
                next_stop = category.get_to_source(number=next_stop)
                break
        return next_stop

    def is_connected_to_a_seed(self, value: int):
        next_stop = value
        for category_type in reversed(self.category_types()):
            next_stop = self.go_to_source(category_type=category_type, number=next_stop)
        for rseed in self.initial_seeds:
            if rseed.start <= next_stop < rseed.end:
                return True
        return False
