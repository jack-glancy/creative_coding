import math
import time
import diet_options as diet


class locations:
    dict = {
        'Hartsfield–Jackson Atlanta International Airport': ('33.6407', '-84.4277'),
        'Beijing Capital International Airport': ('40.0799', '116.6031'),
        'Los Angeles International Airport': ('33.9416', '-118.4085'),
        'Haneda Airport': ('35.5494', '139.7798'),
        'Dubai International Airport': ('25.2532', '55.3657'),
        "O'Hare International Airport": ('41.9742', '-87.9073'),
        'London Heathrow Airport': ('51.4700', '-0.4543'),
        'Shanghai Pudong International Airport': ('31.1443', '121.8083'),
        'Hong Kong International Airport': ('22.3080', '113.9185'),
        'Paris-Charles de Gaulle Airport': ('49.0097', '2.5479'),
        'Dallas/Fort Worth International Airport': ('32.8998', '-97.0403'),
        'Guangzhou Baiyun International Airport': ('23.3959', '113.3080'),
        'Seoul Incheon International Airport': ('37.4602', '126.4407'),
        'Amsterdam Airport Schiphol': ('52.3105', '4.7683'),
        'Frankfurt Airport': ('50.0379', '8.5622'),
        'Singapore Changi Airport': ('1.3644', '103.9915'),
        'Suvarnabhumi Airport': ('13.6900', '100.7501'),
        'Denver International Airport': ('39.8561', '-104.6737'),
        'Indira Gandhi International Airport': ('28.5562', '77.1000'),
        'Soekarno–Hatta International Airport': ('6.1275', '106.6537'),
        'John F. Kennedy International Airport': ('40.6413', '-73.7781'),
        'Kuala Lumpur International Airport': ('2.7456', '101.7072'),
        'Madrid Barajas Airport': ('40.4983', '-3.5676'),
        'San Francisco International Airport': ('37.6213', '-122.3790'),
        'Chengdu Shuangliu International Airport': ('30.5675', '103.9493'),
        "Shenzhen Bao'an International Airport": ('22.6368', '113.8146'),
        'Orlando International Airport': ('28.4312', '-81.3081'),
        'McCarran International Airport': ('36.0840', '-115.1537'),
        'Barcelona–El Prat Airport': ('41.2974', '2.0833'),
        'Toronto Pearson International Airport': ('43.6777', '-79.6248')
    }


class cons:
    km_to_ghg = 0.115 #Kg_CO2/km
    c_out = 0
    c_in = 0
    x = (0, 0)
    y = (0, 0)
    radius = 6371
    dist = 0
    ghg = 0
    first = 1
    beef_to_ghg = 13.3 #Kg_CO2/Kg
    diff = 0
    days = 0
    weeks = 0


def get_start():
    print('Please enter where you\'re travelling from: ')
    cons.c_out = input()


def get_end():
    print('Please enter where you\'re travelling to: ')
    cons.c_in = input()


def lookup_positions(x, y):
    print(x, y)
    start = locations.dict.get(x)
    end = locations.dict.get(y)
    print(start,end)
    x_lat = float(start[0])/180*math.pi
    x_long = float(start[1])/180*math.pi
    y_lat = float(end[0])/180*math.pi
    y_long = float(end[1])/180*math.pi
    angle = math.acos(math.sin(x_lat)*math.sin(y_lat) + math.cos(x_lat)*math.cos(y_lat)*math.cos(y_long - x_long))
    cons.dist = cons.radius*angle


def get_class():
    pass


def calculate_ghg():
    cons.ghg = cons.dist*cons.km_to_ghg*cons.first


def give_options():
    x = round(cons.ghg, 1)
    print('You\'ve flown ' + str(round(cons.dist)) + ' km and generated ' + str(round(cons.ghg, 1)) + ' Kg of CO2 equivalents with your flight.')
    beef = round(x/cons.beef_to_ghg)
    servings = round((x/cons.beef_to_ghg)/0.0860486)
    print('To offset this, you could cut out ' + str(beef) + ' Kg of beef from your diet.')
    print('This is equivalent to ' + str(servings) + ' servings.')


def diet_find(x):
    food = diet.diet_options.dict.get(x)
    vegan = diet.diet_options.dict.get('Vegans')
    cons.diff = food[2] - vegan[2]

def calc_days():
    cons.days = cons.ghg/cons.diff
    cons.weeks = cons.days*7


def main():
    get_start()
    get_end()
    lookup_positions()
    calculate_distance()
    get_class()
    calculate_ghg()
    give_options()


if __name__ == '__main__':
    main()
