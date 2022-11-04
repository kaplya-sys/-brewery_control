from enum import Enum

class ProductType(Enum):
    malt = 'malt'
    hop = 'hop'
    yeast = 'yeast'

    def translate_name(self):
        types = {
            ProductType.malt: 'Солод',
            ProductType.hop: 'Хмель',
            ProductType.yeast: 'Дрожжи'
        }
        return types[self]
    