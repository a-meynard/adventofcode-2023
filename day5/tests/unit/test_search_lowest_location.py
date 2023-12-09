from almanac import Almanac
from category import Category

from search_lowest_location import SearchLowestLocation


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
            Category(name="seed", number=79, destination_numer=50),
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
            Category(name="seed", number=79, destination_numer=50),
            Category(name="seed", number=14, destination_numer=44),
        ],
    )
    assert SearchLowestLocation().handle(almanac=almanac) == 44


def test_search_lowest_location_with_multiple_seed_and_one_category_type_and_useless_categories():
    almanac = Almanac(
        initial_seeds=[79, 16],
        categories=[
            Category(name="seed", number=79, destination_numer=50),
            Category(name="seed", number=14, destination_numer=44),
            Category(name="seed", number=15, destination_numer=45),
            Category(name="seed", number=16, destination_numer=46),
            Category(name="seed", number=17, destination_numer=47),
        ],
    )
    assert SearchLowestLocation().handle(almanac=almanac) == 46


def test_search_lowest_location_with_multiple_seed_and_multiple_category_types():
    almanac = Almanac(
        initial_seeds=[79, 16],
        categories=[
            Category(name="seed", number=79, destination_numer=50),
            Category(name="seed", number=14, destination_numer=44),
            Category(name="seed", number=15, destination_numer=45),
            Category(name="seed", number=16, destination_numer=46),
            Category(name="seed", number=17, destination_numer=47),
            Category(name="soil", number=44, destination_numer=12),
            Category(name="soil", number=45, destination_numer=13),
            Category(name="soil", number=46, destination_numer=14),
        ],
    )
    assert SearchLowestLocation().handle(almanac=almanac) == 14
