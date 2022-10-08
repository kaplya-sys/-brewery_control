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
        volume == 1050
    return volume
