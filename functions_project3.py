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
screen.setup(width=1.0, height=1.0)

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
def visit(name, rand=None):
    if name in list_cafes:
        if name in paths.keys():
            person.speed(1)
            circ = 0
            for i in paths[name]:
                if i != 'c':
                    person.goto(sq_size * control_points[i][0], sq_size * control_points[i][1])
                else:
                    c(circles[circ][0], circles[circ][1])
                    circ += 1
            person.color('green')
            person.stamp()
            person.penup()
            person.hideturtle()
            person.setheading(90)
            person.fd(10)
            person.color('blue')
            if name.lower() == 'khan-buz' or name.lower() == 'uncle dohner':
                if rand:
                    person.write('There`s the eating spot we`ve come up with: {}'.format(name.title()),
                                 font=('Arial', 14))
                else:
                    person.write('There`s the eating spot you wanted to go to!', font=('Arial', 14))
            elif name.lower() == 'murchim' or name.lower() == 'myasoroob' or name.lower() == 'coffee academy':
                if rand:
                    person.write('There`s the eating spot we`ve come up with: {}'.format(name.title()),
                                 align='right', font=('Arial', 14))
                else:
                    person.write('There`s the eating spot you wanted to go to!', align='right', font=('Arial', 14))
            else:
                if rand:
                    person.write('There`s the eating spot we`ve come up with: {}'.format(name.title()), align='center',
                                 font=('Arial', 14))
                else:
                    person.write('There`s the eating spot you wanted to go to!', align='center', font=('Arial', 14))
        else:
            person.write('We didn`t draw the path yet or there`s no such cafe in Academ', font=('Arial', 16))
    else:
        answer = screen.textinput('Oops, we didn`t find the cafe!',
                                  'Would you like us to consider the path later? ')
        if answer.lower() == 'yes':
            list_cafes.append(name)

    # Recording the new list to csv
    with open('cafes.csv', 'w') as file:
        for i in list_cafes:
            file.write(i + '\n')
