from p5 import *
import numpy as np
from neutron import *
from PIL import ImageFont


class Cons:
    height = 800
    width = 800
    neutrons = []
    counter = 0
    fuel = []
    explosion_parts = 3
    starting_neuts = 10
    control_rods = []
    rods_pos = [(0, 20), (0, height - 60), (width-100, 20), (width-100, height - 60)]


def setup():
    size(Cons.height, Cons.width)
    no_stroke()
    text_align('CENTER')
    background(204)
    for i in range(Cons.starting_neuts):
        Cons.neutrons.append(Neutron([p5.sketch.size[0]/2 + np.random.randint(-10,10), p5.sketch.size[1]/2 + np.random.randint(-10,10)]))
    for i in range(18):
        Cons.fuel.append(Fuel(i))
    for i in range(4):
        Cons.control_rods.append(Control_rod(20, 100, Cons.rods_pos[i]))



def draw():
    if mouse_is_pressed:
        for i in Cons.control_rods:
            i.w += i.w*0.1
    # rect((100,200), 50, 50)
    for i in Cons.neutrons:
        i.show()
        i.check_wall_collision()
        i.update()
        if i.check_collision(Cons.fuel):
            for j in range(Cons.explosion_parts):
                Cons.neutrons.append(Neutron(i.p))
            Cons.neutrons.remove(i)
        if i.check_collision(Cons.control_rods):
            Cons.neutrons.remove(i)
    for i in Cons.fuel:
        i.show()
    for i in Cons.control_rods:
        i.show()
    background(200)
    fill(0)
    text_font(ImageFont.truetype("arial.ttf", 25))
    text("Neutrons:" + str(len(Cons.neutrons)), (p5.sketch.size[0] - 100, 100))


if __name__ == '__main__':
    run()
