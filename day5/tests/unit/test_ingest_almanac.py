from category import Category
from ingest_almanac import IngestAlmanac


def test_ingest_almanac_show_correct_categories_with_multiple_category_type():
    input = [
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "",
        "soil-to-fertilizer map:",
        "15 0 3",
    ]
    usecase = IngestAlmanac()
    almanac = usecase.ingest(input=input)
    assert almanac.categories == [
        Category(name="seed", number=98, destination_numer=50),
        Category(name="seed", number=99, destination_numer=51),
        Category(name="soil", number=0, destination_numer=15),
        Category(name="soil", number=1, destination_numer=16),
        Category(name="soil", number=2, destination_numer=17),
    ]


def test_ingest_almanac_show_correct_categories_with_one_category_type():
    input = [
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 4",
    ]
    usecase = IngestAlmanac()
    almanac = usecase.ingest(input=input)
    assert almanac.categories == [
        Category(name="seed", number=98, destination_numer=50),
        Category(name="seed", number=99, destination_numer=51),
        Category(name="seed", number=50, destination_numer=52),
        Category(name="seed", number=51, destination_numer=53),
        Category(name="seed", number=52, destination_numer=54),
        Category(name="seed", number=53, destination_numer=55),
    ]


def test_ingest_almanac_show_correct_initial_seeds():
    input = [
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 4",
    ]
    usecase = IngestAlmanac()
    almanac = usecase.ingest(input=input)
    assert almanac.initial_seeds == [79, 14, 55, 13]
