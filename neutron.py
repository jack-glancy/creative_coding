from p5 import *
from vector_2d import Vector

class Neutron:
    def __init__(self, p):
        self.r = 10
        self.v = [np.random.randint(-10,10), np.random.randint(-10,10)]
        self.p = p

    def show(self):
        fill(255, 100, 100, 100)
        circle((self.p[0], self.p[1]), self.r)

    def update(self):
        self.p = np.add(self.p, self.v)

    def check_collision(self, others):
        for i in others:
            if hasattr(i, 'r'):
                d = dist(self.p, i.p)
                if d*10 <= self.r + i.r:
                    return True
            elif hasattr(i, 'h'):
                if i.p[0] < self.p[0] <= i.p[0] + i.w and i.p[1] < self.p[1] <= i.p[1] + i.h:
                    return True

    def check_wall_collision(self):
        if self.p[0] - self.r < 0:
            self.p[0] = self.r
            self.v[0] = -self.v[0]
        if self.p[0] + self.r > p5.sketch.size[0]:
            self.p[0] = p5.sketch.size[0] - self.r
            self.v[0] = -self.v[0]
        if self.p[1] - self.r < 0:
            self.p[1] = self.r
            self.v[1] = -self.v[1]
        if self.p[1] + self.r > p5.sketch.size[1]:
            self.p[1] = p5.sketch.size[1] - self.r
            self.v[1] = -self.v[1]


class Fuel:
    def __init__(self, i):
        self.i = i
        self.r = 30
        self.p = (p5.sketch.size[0]/2 + 300*np.cos(i*20*PI/180), p5.sketch.size[1]/2 + 300*np.sin(i*PI/180*20))

    def show(self):
        fill(100, 255, 100, 300)
        circle((self.p[0], self.p[1]), self.r)


class Control_rod:
    def __init__(self, h, w, p):
        self.h = h
        self.w = w
        self.p = p

    def show(self):
        fill(100, 255, 255, 300)
        rect(self.p[0], self.p[1], self.w, self.h)
