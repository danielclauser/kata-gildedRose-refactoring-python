import pytest
import sys
from src.gilded_rose.gilded_rose import Item, GildedRose

def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert "foo" == items[0].name