from turtle import *
import pandas as pd
from control_points_project3 import *

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
cafes = pd.read_csv('cafes.csv', header=None)
list_cafes = []
for k in cafes[0]:
    list_cafes.append(k)


# Making thigs easier when drawing a circle
def c(radius, angle):
    person.circle(radius, angle)


# Main function for drawing the route
def visit(name):
    if name in list_cafes:
        if name in paths.keys():
            circ = 0
            for i in paths[name]:
                if i != 'c':
                    person.goto(sq_size * control_points[i][0], sq_size * control_points[i][1])
                else:
                    c(circles[circ][0], circles[circ][1])
                    circ += 1
        else:
            person.write('We didn`t draw the path yet or there`s no such cafe in Academ')
    else:
        answer = screen.textinput('Oops, we didn`t find the cafe you`ve entered!',
                                  'Would you like us to consider the path later? ')
        if answer == 'yes':
            list_cafes.append(name)

    # Recording the new list to csv
    with open('cafes.csv', 'w') as file:
        for i in list_cafes:
            file.write(i + '\n')
