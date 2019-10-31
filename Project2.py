import math

# The beginning header
print('''Эта программа предлагает Вам познакомиться с треугольниками Пифагора - прямоугольными треугольниками 
с целочисленными сторонами. Программа найдет все пифагорейские тройки в заданном Вами диапазоне.\n''')

while True:
    # Inviting the user to pick a range from where the program will search for Pythagoras triangles
    tr_range = input('Пожалуйста, выберите диапазон для поиска (введите два числа через пробел): ').split(sep=' ')
    start = int(tr_range[0])
    end = int(tr_range[1])

    # "Fool-checking"
    if start > end:
        start, end = end, start

    if start == 0:
        start = 1

    if start >= 0 and end >= 0:
        break
    else:
        print('Вы неверно ввели диапазон. Пожалуйста, попробуйте еще раз.\n')

# Initializing the Pythagoras search
tr_list = []
for a in range(start, end + 1):
    for b in range(start, end + 1):
        c = math.sqrt(a ** 2 + b ** 2)
        if int(c) == c:
            c = int(c)
            list12 = [a, b]
            list12 = sorted(list12)
            list1 = list12 + [c]
            list1 = str(list1)
            tr_list.append(list1)

ordered = list(dict.fromkeys(tr_list))

# Printing out the result
if not ordered:
    print('В заданном диапазоне не существует пифагорейских треугольников.')
else:
    print('В заданном диапазоне существуют треугольники Пифагора со следующими тройками сторон:')
    for i in ordered:
        print(i)
