from tkinter import *
import numpy as np
from scipy.interpolate import interp1d


class Cons:
    canvwidth = 1000
    canvheight = 1000
    numdrops = 1000

class Drop:
    def __init__(self):
        self.x = np.random.randint(0,1000)
        self.y = np.random.randint(-2000, -100)
        self.z = np.random.randint(1,200)
        m = interp1d([1, 200], [10, 40])
        self.yspeed = m(self.z)
        self.line = None

    def fall(self):
        self.y += self.yspeed
        if self.y > Cons.canvheight:
            self.y = np.random.randint(-200, -100)

    def show(self):
        myCanvas.delete(self.line)
        self.line = myCanvas.create_line(self.x, self.y, self.x, self.y + 10, width=self.z/100, fill='purple')


def update():
    for i in drops:
        i.fall()
        i.show()
    root.after(10, update)

root = Tk()
myCanvas = Canvas(root, height=Cons.canvheight, width=Cons.canvwidth)
myCanvas.pack()
drops = []
for i in range(Cons.numdrops):
    drop = Drop()
    drops.append(drop)


def main():
    root.after(1000, update)
    root.mainloop()


if __name__ == '__main__':
    main()
