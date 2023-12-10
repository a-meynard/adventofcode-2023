from almanac import Almanac
from category import Category, CategoryV2
from feature_router import FeatureRouter
from range_seed import RangeSeed

from search_lowest_location import SearchLowestLocation

from dataclasses import dataclass


@dataclass(frozen=True)
class Range:
    start: int
    end: int


def build_categories_from_range(
    name: str, numbers: Range, destinations: Range
) -> list[Category] | list[CategoryV2]:
    if FeatureRouter.ENABLE_CATEGORY_V2:
        return [
            CategoryV2(
                name=name,
                source_start=numbers.start,
                destination_start=destinations.start,
                range_length=(numbers.end - numbers.start + 1),
            )
        ]
    else:
        return [
            Category(
                name=name,
                number=numbers.start + i,
                destination_numer=destinations.start + i,
            )
            for i in range(numbers.end - numbers.start + 1)
        ]


def test_search_lowest_location_with_one_seed_no_category():
    almanac = Almanac(
        initial_seeds=[79],
        categories=[],
    )
    assert SearchLowestLocation().handle(almanac=almanac) == 79


def test_search_lowest_location_with_one_seed_and_one_category_type():
    almanac = Almanac(
        initial_seeds=[79],
        categories=[
            *build_categories_from_range(
                name="seed", numbers=Range(79, 79), destinations=Range(50, 50)
            )
        ],
    )
    assert SearchLowestLocation().handle(almanac=almanac) == 50


def test_search_lowest_location_with_multiple_seed_and_no_category_type():
    almanac = Almanac(
        initial_seeds=[79, 14],
        categories=[],
    )
    assert SearchLowestLocation().handle(almanac=almanac) == 14


def test_search_lowest_location_with_multiple_seed_and_one_category_type():
    almanac = Almanac(
        initial_seeds=[79, 14],
        categories=[
            *build_categories_from_range(
                name="seed", numbers=Range(79, 79), destinations=Range(50, 50)
            ),
            *build_categories_from_range(
                name="seed", numbers=Range(14, 14), destinations=Range(44, 44)
            ),
        ],
    )
    assert SearchLowestLocation().handle(almanac=almanac) == 44


def test_search_lowest_location_with_multiple_seed_and_one_category_type_and_useless_categories():
    almanac = Almanac(
        initial_seeds=[79, 16],
        categories=[
            *build_categories_from_range(
                name="seed", numbers=Range(79, 79), destinations=Range(50, 50)
            ),
            *build_categories_from_range(
                name="seed", numbers=Range(14, 17), destinations=Range(44, 47)
            ),
        ],
    )
    assert SearchLowestLocation().handle(almanac=almanac) == 46


def test_search_lowest_location_with_multiple_seed_and_multiple_category_types():
    almanac = Almanac(
        initial_seeds=[79, 16],
        categories=[
            *build_categories_from_range(
                name="seed", numbers=Range(79, 79), destinations=Range(50, 50)
            ),
            *build_categories_from_range(
                name="seed", numbers=Range(14, 17), destinations=Range(44, 47)
            ),
            *build_categories_from_range(
                name="soil", numbers=Range(44, 46), destinations=Range(12, 14)
            ),
        ],
    )
    assert SearchLowestLocation().handle(almanac=almanac) == 14


def test_search_lowest_location_with_multiple_seed_and_multiple_category_types():
    FeatureRouter.ENABLE_RANGE_SEED = True
    almanac = Almanac(
        initial_seeds=[RangeSeed(79, 80), RangeSeed(44, 46)],
        categories=[
            *build_categories_from_range(
                name="seed", numbers=Range(79, 79), destinations=Range(12, 12)
            ),
            *build_categories_from_range(
                name="seed", numbers=Range(44, 46), destinations=Range(70, 72)
            ),
            *build_categories_from_range(
                name="soil", numbers=Range(12, 12), destinations=Range(16, 16)
            ),
        ],
    )
    assert SearchLowestLocation().handle(almanac=almanac) == 16
    FeatureRouter.ENABLE_RANGE_SEED = False
