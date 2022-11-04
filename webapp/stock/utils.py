from webapp.stock.enums import ProductType

malt_range = [
    'Pilsner (SП) (40 кг.)',
    'Pilsner Premium (SП) (25 кг.)',
    'Pale Ale (SП) (40 кг.)',
    'Пшеничный (SП) (40 кг.)',
    'Мюнхенский (15 EBC) (SП) (40 кг.)',
    'Мюнхенский (25 EBC) (SП) (40 кг.)',
    'Жженый (1200-1400) (SП) (25 кг.)',
    'Cara Clair (6 EBC) (CM) (25 кг.)',
    'Melano (80 EBC) (CM) (25 кг.)',
    'Crystal (150 EBC) (CM) (25 кг.)',

]
hop_range = [
    'Cascade (HCA) (6,0)',
    'Mandarina (HMBA) (7,5)',
    'Mittelfruh (HHAL) (5,5)',
    'Nugget (HNUG) (11,3)',
    'Perle (HPER) (6,9)',
    'Sp. Select (HSSE) (5,2)',
]
yeasts_range = [
    'Fermentis 34/70',
    'Fermentis WB-06',
    'Fermentis K-97',
    'Fermentis SafCider',
]

def get_the_right_product(type):
    if type == ProductType.malt.name:
        return malt_range
    elif type == ProductType.hop.name:
        return hop_range
    elif type == ProductType.yeast.name:
        return yeasts_range
    else:
        return None
