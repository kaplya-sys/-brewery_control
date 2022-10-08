from enum import Enum


class TitleBeer(Enum):
    kellerbier = 'kellerbier'
    dunkelbier = 'dunkelbier'
    bropils = 'bropils'
    wheatbeer = 'wheatbeer'
    traditional_dark = 'traditional_dark'
    traditional_light = 'traditional_light'
    traditional_wheat = 'traditional_wheat'
    cider = 'cider'


    def product_name(self):
        product = ''
        if self == TitleBeer.kellerbier:
            product = 'Kellerbier'
        elif self == TitleBeer.dunkelbier:
            product ='Dunkelbier'
        elif self == TitleBeer.bropils:
            product =  'Bro Pils'
        elif self == TitleBeer.wheatbeer:
            product =  'Пшеничное'
        elif self == TitleBeer.traditional_dark:
            product = 'Традиционное Темное'
        elif self == TitleBeer.traditional_light:
            product = 'Традиционное Светлое'
        elif self == TitleBeer.traditional_wheat:
            product = 'Традиционное Пшеничное'
        elif self == TitleBeer.cider:
            product = 'Пивной напиток',
        return product
