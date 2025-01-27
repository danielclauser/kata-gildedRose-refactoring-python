class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name not in {
                "Aged Brie",
                "Backstage passes to a TAFKAL80ETC concert",
            }:
                if item.quality > 0 and item.name != "Sulfuras, Hand of Ragnaros":
                    item.quality = item.quality - 1
            elif item.quality < 50:
                item.quality = item.quality + 1
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11 and item.quality < 50:
                        item.quality = item.quality + 1
                    if item.sell_in < 6 and item.quality < 50:
                        item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if (
                            item.quality > 0
                            and item.name != "Sulfuras, Hand of Ragnaros"
                        ):
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
        return f"{self.name}, {self.sellin}, {self.quality}"
