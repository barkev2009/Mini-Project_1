from functions_project3 import *

person.penup()
person.goto(-46*sq_size, 26*sq_size)
person.pendown()

place = screen.textinput('Make the choice)',
                         'What eating point would you want to go to?')
visit(place)
