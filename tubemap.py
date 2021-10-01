from p5 import *
import pandas as pd
import math
from PIL import ImageFont


class Cons:
    width = 1500
    height = 1000
    k = 0
    l = 0
    xy = []
    lines = []
    dfs = []
    prev_x = None
    prev_y = None

df = pd.read_csv('C:/Users/jjg52/Desktop/Work/Python/tube/tube_data.csv')
#print(df[['x', 'y', 'LINES']])
for i in df['LINES']:
    split = str(i).split(', ')
    for lyne in split:
        if lyne in Cons.lines:
            pass
        else:
            Cons.lines.append(lyne)

#print(Cons.lines)
for lyne in Cons.lines:
    if lyne == 'nan':
        pass
    else:
        criterion = df['LINES'].map(lambda x: lyne in str(x))
        df2 = df[criterion]
        Cons.dfs.append(df2)

for i in Cons.dfs:
    for j in range(len(i)):
        print(i.iloc[j]['x'])


with open('C:/Users/jjg52/Desktop/Work/Python/tube/xy.txt', 'r') as f:
    lynes = f.readlines()

for lyne in Cons.lines:
    split = lyne.split()
    Cons.xy.append(split)


def setup():
    size(Cons.width, Cons.height)
    fill(random_uniform(0, 255), random_uniform(0, 255), random_uniform(0, 255))


def draw():
    if Cons.k < len(Cons.lines) - 1:
        text_font(ImageFont.truetype("arial.ttf", 25))
        text("Line:" + Cons.lines[Cons.k], (p5.sketch.size[0] - 300, 100))
        df = Cons.dfs[Cons.k]
        if Cons.l < len(Cons.dfs[Cons.k]):
            x = (df.iloc[Cons.l]['x'] + 0.127965578)*1500 + Cons.width/2
            y = -(df.iloc[Cons.l]['y'] - 51.52408837)*3000 + Cons.height/2
            #print(x, y)
            if not math.isnan(x):
                circle(x, y, 5)
            # if Cons.prev_x is not None:
            #     if dist((x, y), (Cons.prev_x, Cons.prev_y)) < 100:
            #         line((x, y), (Cons.prev_x, Cons.prev_y))
            Cons.prev_x = x
            Cons.prev_y = y
            Cons.l += 1
        else:
            Cons.l = 0
            no_stroke()
            fill(204)
            rect(p5.sketch.size[0] - 300, 150, 300, -150)
            stroke(0)
            fill(random_uniform(0, 255), random_uniform(0, 255), random_uniform(0, 255))
            print(Cons.lines[Cons.k])
            Cons.k += 1
            Cons.prev_x = None
            Cons.prev_y = None
            # if Cons.k < len(Cons.xy) - 1:
            #     circle((float(Cons.xy[Cons.k][0]) - -0.127965578)*1000 + Cons.width/2, (float(Cons.xy[Cons.k][1]) - 51.52408837)*2500 + Cons.height/2, 5)
            # Cons.k += 1
    else:
        pass


run()
