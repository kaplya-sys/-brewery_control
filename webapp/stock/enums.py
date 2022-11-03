from enum import Enum

class ProductType(Enum):
    malt = 'malt'
    hop = 'hop'
    yeast = 'yeast'
    other = 'other'

    def type_name(self):
        types = {
            ProductType.malt: 'Солод',
            ProductType.hop: 'Хмель',
            ProductType.yeast: 'Дрожжи',
            ProductType.other: 'Другое'
        }
        return types[self]
    