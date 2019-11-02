from math import *


def deletion_process(delete_indexes, dots):
    k_s = []
    deletions = []
    for k in delete_indexes.keys():
        first = int(k.split(sep=' ')[0])
        second = int(k.split(sep=' ')[1])
        deletion = int(
            input('Dots {} and {} are close to each other, which one should I delete? '.format(first, second)))
        if deletion == 0:
            continue
        else:
            dots.pop(deletion)
            k_s.append(k)
            deletions.append(deletion)

    for k in k_s:
        del delete_indexes[k]

    k_s1 = []
    for i in deletions:
        for k in delete_indexes.keys():
            first = int(k.split(sep=' ')[0])
            second = int(k.split(sep=' ')[1])
            if i == first or i == second:
                k_s1.append(k)
    for k in k_s1:
        del delete_indexes[k]


def form_deletion_indexes(dots):
    distances = {}
    delete_indexes = {}
    for i1 in range(1, len(dots) + 1):
        for i2 in range(1, len(dots) + 1):
            if i1 == i2:
                continue
            else:
                distance = sqrt((dots[i2][0] - dots[i1][0]) ** 2 +
                                (dots[i2][1] - dots[i1][1]) ** 2 +
                                (dots[i2][2] - dots[i1][2]) ** 2)
                key = '{} {}'.format(i1, i2)
                distances[key] = distance
                if distance < 3 and i1 < i2:
                    delete_indexes[key] = distance
    return delete_indexes


def create_dots(number):
    dots = {}
    for i in range(number):
        choice = input('Type in the {} dot-coordinates through SPACE: '.format(i+1)).split(sep=' ')
        dot = []
        for each in choice:
            a = int(each)
            dot.append(a)
        dots[i+1] = dot
    return dots
