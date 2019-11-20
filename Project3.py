from functions_project3 import *
from random import randint

inf = 'yes'
while inf.lower() != 'no':
    # Creating person
    person.reset()
    person.shape('circle')
    person.pensize(3)
    person.color('red')
    person.speed(0)
    person.penup()
    person.goto(-46 * sq_size, 26 * sq_size)
    person.pendown()

    randor = screen.textinput('Initial choice', 'Do you know what place to go to?')
    if randor.lower() == 'yes':
        place = screen.textinput('Make the main choice)',
                                 'What eating point would you want to go to?')
        visit(place)
    else:
        name = randint(0, len(paths)-1)
        visit(list_cafes[name], True)

    inf = screen.textinput('Would you like to choose another route?', 'Once again?')
