from functions_project3 import *
from random import randint

person.penup()
person.goto(-46 * sq_size, 26 * sq_size)
person.pendown()

randor = screen.textinput('Initial choice', 'Do you know what place to go to?')
if randor.lower() == 'yes':
    place = screen.textinput('Make the main choice)',
                             'What eating point would you want to go to?')
    visit(place)
else:
    name = randint(0, len(paths))
    visit(list_cafes[name], True)
