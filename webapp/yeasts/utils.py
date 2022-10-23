from webapp.yeasts.enums import TypeOfYeast
from webapp.tank.enums import TitleBeer
from webapp.yeasts.models import Yeasts


def get_the_right_yeasts(beer_name): 
    type_of_beer = TitleBeer(beer_name)
    yeast_34_70 = [
        TitleBeer.kellerbier,
        TitleBeer.dunkelbier,
        TitleBeer.bropils,
        TitleBeer.traditional_light,
        TitleBeer.traditional_dark]
    if type_of_beer in yeast_34_70:
        return TypeOfYeast.w_34_70
    elif type_of_beer == TitleBeer.wheatbeer:
        return TypeOfYeast.wb_06
    elif type_of_beer == TitleBeer.traditional_wheat:
        return TypeOfYeast.k_97
    elif type_of_beer == TitleBeer.cider:
        return TypeOfYeast.maxifarm


def is_the_generation_suitable(type_yeast, generate_yeast):
    if type_yeast != TypeOfYeast.w_34_70 and generate_yeast >= 1:
        return False
    if generate_yeast >= 6:
        return False
    else:
        return True


def get_list_of_suitable_tanks(yeasts):
    list_tanks = []
    yeastObjects = Yeasts.query.filter(Yeasts.name == yeasts)
    for yeast in yeastObjects:
        tanks = yeast.tanks
        if is_the_generation_suitable(yeast.name, yeast.cycles):
            for tank in tanks:
                list_tanks.append([f'#{tank.number} {tank.title.product_name()} др. {yeast.name.value} ген. {yeast.cycles}-я  /{yeast.id}'])
    return list_tanks


def get_id_now_yeast(info_for_yeats):
    positions_id = info_for_yeats.rfind('/') + 1
    try:
        yeast_id = int(info_for_yeats[positions_id:])
    except ValueError:
        return -1, -1
    positions = info_for_yeats.rfind('-') - 1
    generation = int(info_for_yeats[positions])
    return yeast_id, generation
