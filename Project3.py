from project3_functions import *

# Header
print('''Hello! This program invites you to enter the number of dots in 3d space, then it checks the dots and offers
you to delete the dots which are either identical or close to each other. Be careful to use the soft wisely as it's 
far from completely ready and designed)
''')

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
