from webapp.tank.enums import TitleBeer

def number_of_brews_for_full_tank(number_tank):
    """returns the required number of slides to fill the tank"""

    if 1 <= number_tank < 9 or 17 <= number_tank < 19:
        return 2
    elif 9 <= number_tank < 17:
        return 4
    elif 20 <= number_tank < 26:
        return 8
    elif number_tank == 19:
        return 1
        

def planned_expected_volume(number_of_brews):
    """returns the planned tank volume"""

    volume = 1200
    if number_of_brews in range(1, 4):
        volume = 1050
    return volume
 

def get_density_for_grooving(title_beer):
    """returns the required density for beer grooving"""

    if title_beer in [TitleBeer.kellerbier, TitleBeer.dunkelbier, TitleBeer.wheatbeer]:
        return 7.5
    elif title_beer in [TitleBeer.bropils, TitleBeer.traditional_wheat ,TitleBeer.cider]:
        return 6.5
    elif title_beer in [TitleBeer.traditional_dark, TitleBeer.traditional_light]:
        return 6.0


def get_density_for_cooling(title_beer):
    """returns the required density for beer cooling"""

    if title_beer in [TitleBeer.kellerbier, TitleBeer.dunkelbier, TitleBeer.traditional_wheat]:
        return 4.4
    elif title_beer == TitleBeer.wheatbeer:
        return 5.4
    elif title_beer in [TitleBeer.bropils, TitleBeer.cider]:
        return 4
    elif title_beer in [TitleBeer.traditional_dark, TitleBeer.traditional_light]:
        return 3.5


def is_beer_need_grooving(title_beer, density):
    """checking for the need for beer grooving"""

    if density <= get_density_for_grooving(title_beer):
        return True
    return False


def is_beer_need_cooling(title_beer, density):
    """checking for the need for beer cooling"""

    if density <= get_density_for_cooling(title_beer):
        return True
    return False
