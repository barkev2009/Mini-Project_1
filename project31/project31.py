from turtle import *

screen = Screen()
person = Turtle()
person.shape('circle')
person.shapesize(1)
person.color('red')
person.speed(0)

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
         'Pick-Up Coffee']

screen.bgpic('Map.png')
screen_width = 1400
screen_height = 920
sq_size = 20
screen.screensize(screen_width, screen_height)


def grid():
    grid1 = Turtle()
    grid1.speed(0)
    grid1.penup()
    grid1.goto(-screen_width / 2, -screen_height / 2)
    grid1.pendown()

    for i in range(int(screen_height/sq_size)):
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

    for i in range(int(screen_width/sq_size)):
        grid1.forward(screen_height)
        grid1.left(90)
        grid1.forward(sq_size)
        grid1.left(90)
        grid1.forward(screen_height)
        grid1.right(90)
        grid1.forward(sq_size)
        grid1.right(90)


# grid()

person.penup()
person.goto(-23*sq_size, 13*sq_size)
place = textinput('Программа покажет маршрут до кафе, в которое Вы хотите пойти', 'Какое кафе предпочитаете?')

done()
