from paths_project3 import *

screen = Screen()
screen.bgpic('Map.png')
screen_width = 1400
screen_height = 920
sq_size = 10
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
person.goto(-46*sq_size, 26*sq_size)
# place = textinput('Программа покажет маршрут до кафе, в которое Вы хотите пойти', 'Какое кафе предпочитаете?')

person.pendown()
person.goto(control_points[0][0]*sq_size, control_points[0][1]*sq_size)
person.goto(control_points[1][0]*sq_size, control_points[1][1]*sq_size)

done()
