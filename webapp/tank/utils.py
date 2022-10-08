def number_of_brews(number_tank):

    if number_tank in range(1, 9) or number_tank in range(17, 19):
        return 2
    elif number_tank in range(9, 17):
        return 4
    elif number_tank in range(20, 26):
        return 8
    elif number_tank == 19:
        return 1


def expected_volume(number_of_brews):
    volume = 1200
    if number_of_brews in range(1, 4):
        volume == 1050
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


def colling_now_check(title_beer, density):
    """checking for the need for beer cooling"""

    if density <= need_density_for_cooling(title_beer):
        return True
    return False


# def fermentation_stage(title_beer, density, beer_grooving, colling_now):
#     """fermentation stage check"""

#     if colling_now:
#         return colling_now 
#     else:
#         if beer_grooving:
#             return colling_now_check(title_beer, density)
#         else:
#             return beer_grooving_check(title_beer, density)
