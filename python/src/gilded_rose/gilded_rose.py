class Item:
    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self) -> None:
        return f"{self.name}, {self.sell_in}, {self.quality}"


class GildedRose:
    ITEMS_LEGENDARY: set[str] = {"Sulfuras, Hand of Ragnaros"}
    ITEMS_QUALITY_ENHANCED_ON_DEGRADE: set[str] = {
        "Backstage passes to a TAFKAL80ETC concert"
    }
    ITEMS_QUALITY_ONLY_UP_ON_DEGRADE: set[str] = {"Aged Brie"}
    items_no_degrade: set[str] = set.union(
        ITEMS_QUALITY_ONLY_UP_ON_DEGRADE,
        ITEMS_LEGENDARY,
        ITEMS_QUALITY_ENHANCED_ON_DEGRADE,
    )

    def __init__(self, items: list[Item]) -> None:
        self.items = items

    def _item_is_expired(self, item: Item) -> None:
        if item.name in self.ITEMS_QUALITY_ONLY_UP_ON_DEGRADE and item.quality < 50:
            item.quality += 1
        elif item.name in self.ITEMS_QUALITY_ENHANCED_ON_DEGRADE:
            item.quality = 0
        elif item.name not in self.items_no_degrade and item.quality > 0:
            item.quality = item.quality - 1

    def _item_update_sell_in(self, item: Item) -> None:
        if item.name not in self.ITEMS_LEGENDARY:
            item.sell_in = item.sell_in - 1

    def _item_update_quality(self, item: Item) -> None:
        if item.name not in self.items_no_degrade:
            if item.quality > 0:
                item.quality = item.quality - 1
        elif item.quality < 50:
            item.quality = item.quality + 1
            if item.name in self.ITEMS_QUALITY_ENHANCED_ON_DEGRADE:
                if item.sell_in < 11 and item.quality < 50:
                    item.quality = item.quality + 1
                if item.sell_in < 6 and item.quality < 50:
                    item.quality = item.quality + 1

    def run_items_day_passed_event(self) -> None:
        for item in self.items:
            self._item_update_quality(item)
            self._item_update_sell_in(item)
            if item.sell_in < 0:
                self._item_is_expired(item)
