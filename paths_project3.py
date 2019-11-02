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

control_points = [[-43, 25],  # Intersection of Pirogova and Univer Prospect
                  [-60, 4],   # Turning point in the forest
                  [-64, 1],   # Exit off the forest
                  [-65, -3]]  # Khan-Buz location

paths = {'Khan-Buz': [control_points[0],
                      control_points[1],
                      control_points[2],
                      control_points[3]]}


def visit(name):
    for i in paths[name]:
        person.goto(sq_size * i[0], sq_size * i[1])
