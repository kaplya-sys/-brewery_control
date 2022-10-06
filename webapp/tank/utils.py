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