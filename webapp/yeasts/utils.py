from webapp.yeasts.enums import TypeOfYeast
from webapp.tank.enums import TitleBeer
from webapp.yeasts.models import Yeasts


def get_need_yeasts(beer_name):
    beer_name = getattr(TitleBeer, beer_name)
    yeast_34_70 = [
        TitleBeer.kellerbier,
        TitleBeer.dunkelbier,
        TitleBeer.bropils,
        TitleBeer.traditional_light,
        TitleBeer.traditional_light]
    if beer_name in yeast_34_70:
        return TypeOfYeast.w_34_70
    elif beer_name == TitleBeer.wheatbeer:
        return TypeOfYeast.wb_06
    elif beer_name == TitleBeer.traditional_wheat:
        return TypeOfYeast.k_97
    elif beer_name == TitleBeer.cider:
        return TypeOfYeast.maxifarm


def get_list_of_suitable_tanks(yeasts):
    list_tanks = [yeast for yeast in Yeasts.query.filter(Yeasts.name == yeasts)]
    return list_tanks
