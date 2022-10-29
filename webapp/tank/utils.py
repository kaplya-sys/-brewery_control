import base64
from io import BytesIO
from matplotlib.figure import Figure
import numpy
from webapp.tank.enums import TitleBeer
from webapp.tank.models import Tank, Measuring

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


def generate_diagrams(title, temperature, density, pressure, ticks):
    """the function generate a measurement diagram"""
    x = numpy.arange(len(ticks))
    width = 0.3
    fig = Figure()
    ax = fig.subplots()
    rects1 = ax.bar(x - width/2, temperature, width, label='Температура')
    rects2 = ax.bar(x + width/2, density, width, label='Плотность')
    rects3 = ax.bar(x + width + width/2, pressure, width, label='Давление')
    ax.set_ylabel('Масштаб')
    ax.set_title(f"ЦКТ № {title}")
    ax.set_xticks(x, ticks)
    ax.legend()
    ax.bar_label(rects1, padding=2)
    ax.bar_label(rects2, padding=2)
    ax.bar_label(rects3, padding=2)
    ax.set_xbound(-0.43000000000000005, 4.630000000000001)
    fig.tight_layout()

    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"data:image/png;base64,{data}"


def create_diagrams_for_tanks():
    diagrams = {}
    for tank in Tank.query.order_by(Tank.number.asc()):
        create_date = []
        temperature = []
        density = []
        pressure = []
        for measuring in Measuring.query.order_by(Measuring.create_at.desc()).filter(tank.id == Measuring.tank_id).limit(5):
            temperature.append(measuring.temperature)
            pressure.append(measuring.pressure)
            density.append(measuring.density)
            create_date.append(measuring.create_at.strftime("%d-%m-%y,%H:%M"))

        diagrams[tank.id] = generate_diagrams(tank.number, temperature, density, pressure, create_date)
    return diagrams


def generate_tank_id():
    return [(tank.id, f'{tank.number} - {tank.title.product_name()}') for tank in Tank.query.all()]
