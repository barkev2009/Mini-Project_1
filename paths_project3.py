from turtle import *

# Creating screen class
screen = Screen()
screen.bgpic('Map.png')
screen_width = 1400
screen_height = 920
sq_size = 10
screen.screensize(screen_width, screen_height)


# Creating function to draw grid
def grid():
    grid1 = Turtle()
    grid1.speed(0)
    grid1.penup()
    grid1.goto(-screen_width / 2, -screen_height / 2)
    grid1.pendown()

    for i in range(int(screen_height / sq_size)):
        grid1.forward(screen_width)
        grid1.left(90)
        grid1.forward(sq_size)
        grid1.left(90)
        grid1.forward(screen_width)
        grid1.right(90)
        grid1.forward(sq_size)
        grid1.right(90)

    grid1.penup()
    grid1.setheading(-90)
    grid1.goto(-screen_width / 2, screen_height / 2)
    grid1.pendown()

    for i in range(int(screen_width / sq_size)):
        grid1.forward(screen_height)
        grid1.left(90)
        grid1.forward(sq_size)
        grid1.left(90)
        grid1.forward(screen_height)
        grid1.right(90)
        grid1.forward(sq_size)
        grid1.right(90)


# Creating person
person = Turtle()
person.shape('circle')
person.pensize(3)
person.color('red')
person.speed(0)

# Creating list of various places to eat or drink at
cafes = ['Kuzina',
         'Puerto',
         'Coffee Collective',
         'Myasoroob',
         'Teahuppo',
         'Coffee Academy',
         'Spot&Choose'
         'RybaRis',
         'Kotocafe',
         'Clever',
         'Dudnik',
         'Fabrika Pizza',
         'Vilka-Lozhka',
         'Pechki-Lavochki',
         'Shurubor',
         'Pick-Up Coffee',
         'Khan-Buz',
         'Uncle Dohner',
         'Cinnabon',
         'Co.mein']

control_points = [[-43, 25],  # 0: Intersection of Pirogova and Univer Prospect
                  [-60, 4],   # 1: Turning point in the forest
                  [-64, 1],   # 2: Exit off the forest
                  [-65, -3],  # 3: Khan-Buz location
                  [-39, 20],  # 4: Midpoint point on Ilyicha St (before Teahuppo)
                  [-39, 19],  # 5: Turning point from Ilyicha to Teahuppo
                  [-43, 11],  # 6: Turning point straight to Teahuppo
                  [-42, 10],  # 7: Correcting way to Teahuppo
                  [-41, 10],  # 8: Correcting way to Teahuppo
                  []]

paths = {'Khan-Buz': [control_points[0],
                      control_points[1],
                      control_points[2],
                      control_points[3]],
         'Teahuppo': [control_points[0],
                      control_points[4],
                      control_points[5],
                      control_points[6],
                      control_points[7],
                      control_points[8]]}


def visit(name):
    for i in paths[name]:
        person.goto(sq_size * i[0], sq_size * i[1])
