from turtle import *

# Creating screen class
screen = Screen()
screen.bgpic('Map.png')
screen_width = 1400
screen_height = 920
sq_size = 10
screen.screensize(screen_width, screen_height)

# Creating person
person = Turtle()
person.shape('circle')
person.pensize(3)
person.color('red')
person.speed(0)

# Creating list of various places to eat or drink at
cafes = [# 'Kuzina',
         # 'Puerto',
         'Coffee Collective',
         'Myasoroob',
         # 'Teahuppo',
         'Coffee Academy',
         # 'Spot&Choose'
         # 'RybaRis',
         'Kotocafe',
         # 'Clever',
         'Dudnik',
         # 'Fabrika Pizza',
         # 'Vilka-Lozhka',
         # 'Pechki-Lavochki',
         # 'Shurubor',
         # 'Pick-Up Coffee',
         # 'Khan-Buz',
         # 'Uncle Dohner',
         'Cinnabon',
         # 'Co.mein',
         'Art-Pub',
         # 'Sparks',
         ]

control_points = [[-43, 25],    # 0: Intersection of Pirogova and Univer Prospect
                  [-60, 4],     # 1: Turning point in the forest
                  [-64, 1],     # 2: Exit off the forest
                  [-65, -3],    # 3: Khan-Buz location
                  [-39, 20],    # 4: Midpoint point on Ilyicha St (before Teahuppo)
                  [-39, 19],    # 5: Turning point from Ilyicha to Teahuppo
                  [-43, 11],    # 6: Turning point straight to Teahuppo
                  [-42, 10],    # 7: Correcting way to Teahuppo
                  [-41, 10],    # 8: Teahuppo location
                  [-30, 29],    # 9: Turning point to Co.mein from Univer Porspect
                  [-30, 28],    # 10: Co.mein location
                  [-27, 4],     # 11: Turning point from Ilyicha to Rybaris
                  [-30, 3],     # 12: Rybaris location
                  [-19, -6],    # 13: Turning point from Ilyicha to Vilka-Lozhka
                  [-21, -8],    # 14: Crossroads to Vilka and Pechki
                  [-22, -9],    # 15: Vilka-Lozhka location
                  [-21, -11],   # 16: Pechki-Lavochki location
                  [-64, -4],    # 17: Uncle Dohner location
                  [-40, 9],     # 18: Spot&Choose location
                  [-34, 13],    # 19: Turning point from Ilyicha to Pochta
                  [-37, 11],    # 20: Sparks location
                  [-34, 6],     # 21: Turning point before Fabrika Pizza
                  [-35, 5],     # 22: Fabrika Pizza and Pick-Up Coffee
                  [-25, 1],     # 23: Turning point from Ilyicha to Shurubor
                  [-28, -1],    # 24: Shurubor location
                  [0, -32],     # 25: Intersection of Ilyicha and Morskoy
                  [-4, -35],    # 26: Turning point from Morskoy to Kuzina
                  [-5, -34],    # 27: Kuzina and Puerto location
                  [-15, -43.5], # 28: Turning point from Morskoy to Clever
                  [-16, -42],
                  []]

paths = {'Khan-Buz': [0, 1, 2, 3],
         'Uncle Dohner': [0, 1, 2, 3, 17],
         'Teahuppo': [0, 4, 5, 6, 7, 8],
         'Spot&Choose': [0, 4, 5, 6, 7, 18],
         'Co.mein': [0, 9, 10],
         'Rybaris': [0, 11, 12],
         'Vilka-Lozhka': [0, 11, 13, 14, 15],
         'Pechki-Lavochki': [0, 11, 13, 14, 16],
         'Sparks': [0, 4, 19, 20],
         'Fabrika Pizza': [0, 4, 19, 20, 21, 22],
         'Pick-Up Coffee': [0, 4, 19, 20, 21, 22],
         'Shurubor': [0, 11, 23, 24],
         'Kuzina': [0, 25, 26, 27],
         'Puerto': [0, 25, 26, 27],
         'Clever': [0, 25, 28, 29]}


def visit(name):
    for i in paths[name]:
        person.goto(sq_size * control_points[i][0], sq_size * control_points[i][1])
