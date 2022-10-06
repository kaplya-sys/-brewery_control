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

<<<<<<< HEAD

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
=======
    def __init__(self, variable_name):
        self.variable_name = variable_name

    def product_name(self):
        product_names = {
            'kellerbier': 'Kellerbier',
            'dunkelbier': 'Dunkelbier',
            'bropils': 'Bro Pils',
            'wheatbeer': 'Пшеничное',
            'traditional_dark': 'Традиционное Темное',
            'traditional_light': 'Традиционное Светлое',
            'traditional_wheat': 'Традиционное Пшеничное',
            'cider': 'Пивной напиток',
            }
        return product_names[self.variable_name]
>>>>>>> 2873885f857157d88557f4aacaca589065fe8c35
