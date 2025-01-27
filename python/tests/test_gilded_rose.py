import pytest

from src.gilded_rose.gilded_rose import GildedRose, Item


@pytest.fixture
def mock_inventory1_items() -> list[Item]:
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]
    return items


@pytest.fixture
def mock_gilded_rose_inventory1(mock_inventory1_items) -> GildedRose:
    return GildedRose(mock_inventory1_items)


@pytest.mark.parametrize(
    "id_item, sellin, quality",
    [
        (0, 10, 20),
        (1, 2, 0),
        (2, 5, 7),
        (3, 0, 80),
        (4, -1, 80),
        (5, 15, 20),
        (6, 10, 49),
        (7, 5, 49),
        (8, 3, 6),
    ],
)
def test_validate_inventory1_day_0(
    mock_gilded_rose_inventory1, id_item, sellin, quality
):
    assert mock_gilded_rose_inventory1.items[id_item].sell_in == sellin
    assert mock_gilded_rose_inventory1.items[id_item].quality == quality


@pytest.mark.parametrize(
    "id_item, sellin, quality",
    [
        (0, -20, 0),
        (1, -28, 50),
        (2, -25, 0),
        (3, 0, 80),
        (4, -1, 80),
        (5, -15, 0),
        (6, -20, 0),
        (7, -25, 0),
        (8, -27, 0),
    ],
)
def test_validate_inventory1_after_30_days(
    mock_gilded_rose_inventory1, id_item, sellin, quality
):
    for _ in range(0, 30):
        mock_gilded_rose_inventory1.run_items_day_passed_event()
    assert mock_gilded_rose_inventory1.items[id_item].sell_in == sellin
    assert mock_gilded_rose_inventory1.items[id_item].quality == quality


def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.run_items_day_passed_event()
    assert items[0].name == "foo"
    assert items[0].quality == 0
    assert items[0].sell_in == -1
