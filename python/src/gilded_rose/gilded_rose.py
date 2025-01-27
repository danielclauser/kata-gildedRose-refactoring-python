class Item:
    QUALITY_ONLY_UP_ON_DEGRADE: set[str] = {"Aged Brie"}
    QUALITY_ENHANCED_ON_DEGRADE: set[str] = {
        "Backstage passes to a TAFKAL80ETC concert"
    }
    QUALITY_SELL_IN_LOCKED: set[str] = {"Sulfuras, Hand of Ragnaros"}
    name: str
    sell_in: int
    quality: int
    quality_up_on_degrade: bool = False
    quality_no_degrade: bool = False
    quality_enhanced_near_expiration: bool = False
    quality_sell_in_locked: bool = False
    quality_variaton_units: int = -1
    is_expired: bool = False

    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name = name
        self._set_info_item_by_name()
        self.sell_in = sell_in
        self.quality = quality

    def _set_info_item_by_name(self):
        if self.name in self.QUALITY_ONLY_UP_ON_DEGRADE:
            self.quality_up_on_degrade = True
            self.quality_variaton_units = 1
        if self.name in self.QUALITY_SELL_IN_LOCKED:
            self.quality_sell_in_locked = True
        if self.name in self.QUALITY_ENHANCED_ON_DEGRADE:
            self.quality_enhanced_near_expiration = True
        if (
            self.quality_enhanced_near_expiration
            or self.quality_up_on_degrade
            or self.quality_sell_in_locked
        ):
            self.quality_no_degrade = True

    def check_is_expired(self) -> bool:
        if self.sell_in < 0:
            self.is_expired = True
        return self.is_expired

    def __repr__(self) -> None:
        return f"{self.name}, {self.sell_in}, {self.quality}"


class GildedRose:
    MAX_ITEM_QUALITY = 50

    def __init__(self, items: list[Item]) -> None:
        self.items = items

    def _item_is_expired(self, item: Item) -> None:
        if item.quality_up_on_degrade and item.quality < self.MAX_ITEM_QUALITY:
            item.quality += item.quality_variaton_units
        elif item.quality_enhanced_near_expiration:
            item.quality = 0
        elif not item.quality_no_degrade and item.quality > 0:
            item.quality += item.quality_variaton_units

    def _item_update_sell_in(self, item: Item) -> None:
        if not item.quality_sell_in_locked:
            item.sell_in -= 1

    def _item_update_quality(self, item: Item) -> None:
        if not item.quality_no_degrade:
            if item.quality > 0:
                item.quality -= 1
        elif item.quality < 50:
            item.quality += 1
            if item.quality_enhanced_near_expiration:
                if item.sell_in < 11 and item.quality < 50:
                    item.quality += 1
                if item.sell_in < 6 and item.quality < 50:
                    item.quality += 1

    def run_items_day_passed_event(self) -> None:
        for item in self.items:
            self._item_update_quality(item)
            self._item_update_sell_in(item)
            item.check_is_expired()
            if item.is_expired:
                self._item_is_expired(item)
