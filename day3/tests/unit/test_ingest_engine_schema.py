from schema import Schema
from engine_part import EnginePart
from position import Position
from part_number import PartNumber

from ingest_engine_schema import IngestEngineSchema


def test_ingest_engine_schema_with_only_space():
    raw_schema = ["."]
    usecase = IngestEngineSchema()

    assert usecase.handle(raw_schema=raw_schema) == Schema(
        symbols=set(),
        part_numbers=set(),
    )


def test_ingest_engine_schema_with_only_single_digit_part_numbers():
    raw_schema = ["1"]
    usecase = IngestEngineSchema()

    assert usecase.handle(raw_schema=raw_schema) == Schema(
        symbols=set(),
        part_numbers={
            PartNumber(id=1, position=Position(start=0, end=0, line=0)),
        },
    )


def test_ingest_engine_schema_with_only_engine_part():
    raw_schema = ["*"]
    usecase = IngestEngineSchema()

    assert usecase.handle(raw_schema=raw_schema) == Schema(
        symbols={EnginePart(position=Position(start=0, end=0, line=0))},
        part_numbers=set(),
    )


def test_ingest_engine_schema_with_only_multi_digit_part_numbers():
    raw_schema = ["123."]
    usecase = IngestEngineSchema()

    assert usecase.handle(raw_schema=raw_schema) == Schema(
        symbols=set(),
        part_numbers={
            PartNumber(id=123, position=Position(start=0, end=2, line=0)),
        },
    )


def test_ingest_engine_schema_with_multiple_lines():
    raw_schema = ["123.", "*..0"]
    usecase = IngestEngineSchema()

    assert usecase.handle(raw_schema=raw_schema) == Schema(
        symbols={EnginePart(position=Position(start=0, end=0, line=1))},
        part_numbers={
            PartNumber(id=123, position=Position(start=0, end=2, line=0)),
            PartNumber(id=0, position=Position(start=3, end=3, line=1)),
        },
    )


def test_ingest_engine_schema_with_symbol_between_part_numbers():
    raw_schema = ["123*12"]
    usecase = IngestEngineSchema()

    assert usecase.handle(raw_schema=raw_schema) == Schema(
        symbols={EnginePart(position=Position(start=3, end=3, line=0))},
        part_numbers={
            PartNumber(id=123, position=Position(start=0, end=2, line=0)),
            PartNumber(id=12, position=Position(start=4, end=5, line=0)),
        },
    )


def test_ingest_engine_schema_with_gear_symbol():
    raw_schema = ["*"]
    usecase = IngestEngineSchema()

    assert usecase.handle(raw_schema=raw_schema) == Schema(
        symbols={EnginePart(position=Position(start=0, end=0, line=0), is_gear=True)},
        part_numbers=set(),
    )
