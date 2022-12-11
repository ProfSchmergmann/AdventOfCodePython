import pytest

from days.day1 import Day1


def test_day1_part_a():
    day = Day1()
    assert day.part_a() == 69206


def test_day1_part_b():
    day = Day1()
    assert day.part_b() == 197400
