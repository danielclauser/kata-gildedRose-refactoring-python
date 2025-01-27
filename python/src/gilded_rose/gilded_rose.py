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

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
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
            if item.name not in self.ITEMS_LEGENDARY:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name not in self.ITEMS_QUALITY_ONLY_UP_ON_DEGRADE:
                    if item.name not in self.ITEMS_QUALITY_ENHANCED_ON_DEGRADE:
                        if item.quality > 0 and item.name not in self.ITEMS_LEGENDARY:
                            item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                elif item.quality < 50:
                    item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"
