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
 

def need_density_for_grooving(title_beer):
    """returns the required density for beer grooving"""

    if title_beer in ['kellerbier', 'dunkelbier', 'wheatbeer']:
        return 7.5
    elif title_beer in ['bropils', 'traditional_wheat', 'cider']:
        return 6.5
    elif title_beer in ['traditional_dark', 'traditional_light']:
        return 6.0


def need_density_for_cooling(title_beer):
    """returns the required density for beer cooling"""

    if title_beer in ['kellerbier', 'dunkelbier', 'traditional_wheat']:
        return 4.4
    elif title_beer == 'wheatbeer':
        return 5.4
    elif title_beer in ['bropils', 'cider']:
        return 4
    elif title_beer in ['traditional_dark', 'traditional_light']:
        return 3.5


def beer_grooving_check(title_beer, density):
    """checking for the need for beer grooving"""

    if density <= need_density_for_grooving(title_beer):
        return True
    return False


def cooling_beer_check(title_beer, density):
    """checking for the need for beer cooling"""

    if density <= need_density_for_cooling(title_beer):
        return True
    return False
