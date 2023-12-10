from dataclasses import dataclass, field

from category import Category, CategoryV2


@dataclass
class Almanac:
    initial_seeds: list[int] = field(default_factory=list)
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
