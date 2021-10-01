from p5 import *
import numpy as np

class Cons:
    width = 1600
    height = 800
    pm = None
    flake_imgs = []
    flakes = []

class Flake():
    def __init__(self):
        self.p = ((random_uniform(p5.sketch.size[0] / 2, p5.sketch.size[0] / 2 + 100)), -200)
        self.img = Cons.flake_imgs[np.random.randint(0, len(Cons.flake_imgs))]
        self.v = (0, random_uniform(1, 3))
        self.angle = 0

    def show(self):
        image(self.img, self.p[0], self.p[1])

    def update(self):
        self.p = np.add(self.p, self.v)
        self.angle += PI/180
        if self.p[1] >= p5.sketch.size[1]:
            Cons.flakes.remove(self)

def setup():
    size(Cons.width, Cons.height)
    stroke(0)
    stroke_weight(1)

def draw():
    no_fill()
    bbox = rect(100, 100, p5.sketch.size[0]/4 - 200, p5.sketch.size[1]/2 - 200)
    #line(p5.sketch.size[0]/2, 0, p5.sketch.size[0]/2, p5.sketch.size[1])
    if 100 < mouse_x < p5.sketch.size[0] / 4 - 200 and 100 < mouse_y < p5.sketch.size[1]/2 - 200:
        if mouse_is_pressed:
            translate(p5.sketch.size[0] / 8, p5.sketch.size[1] / 4)
            stroke(255)
            stroke_weight(random_uniform(4, 10))
            if Cons.pm:
                mx = mouse_x - p5.sketch.size[0] / 8
                my = mouse_y - p5.sketch.size[1] / 4
                pmx = Cons.pm[0] - p5.sketch.size[0] / 8
                pmy = Cons.pm[1] - p5.sketch.size[1] / 4
                for i in range(6):
                    angle = i * PI / 3
                    rotate(angle)
                    line((mx, my), (pmx, pmy))
                    scale(1, -1)
                    line((mx, my), (pmx, pmy))
            Cons.pm = (mouse_x, mouse_y)
    stroke(0)
    stroke_weight(1)

    if Cons.flake_imgs:
        if len(Cons.flakes) < 5:
            Cons.flakes.append(Flake())

    for i in Cons.flakes:
        i.show()
        i.update()
    fill(204)
    #rect(p5.sketch.size[0] / 2, 0, p5.sketch.size[0], p5.sketch.size[1])

    if key == 'DELETE':
        background(204)
        Cons.pm = None

    if key == 's':
        with load_pixels():
            translate(0,0)
            # pixels only available when load_pixels in play
            pix = pixels
        x2 = int(p5.sketch.size[0] / 4 - 100) - 1
        y2 = int(p5.sketch.size[1] / 2 - 100) - 10
        img = pix[101:x2, 101:y2]
        Cons.flake_imgs.append(img)

run()
