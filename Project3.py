from project3_functions import *

# Creating the dictionary of dots
number = int(input('How many dots do you want to enter? '))
dots = create_dots(number)

print(dots)

# Creating the dictionary of distances of close-related dots
delete_indexes = form_deletion_indexes(dots)

print(delete_indexes)

# Deleting the close-related dots
while delete_indexes:
    deletion_process(delete_indexes, dots)
    print(delete_indexes)

print(dots)
