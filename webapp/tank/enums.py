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
