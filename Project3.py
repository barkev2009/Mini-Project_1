from functions_project3 import *

person.penup()
person.goto(-46*sq_size, 26*sq_size)
person.pendown()

place = screen.textinput('Программа покажет маршрут до кафе, в которое Вы хотите пойти', 'Какое кафе предпочитаете?')
visit(place)
