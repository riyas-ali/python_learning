import math


def paint_calculation(height, width, cover):
    area = height * width
    no_of_cans = math.ceil(area / cover)
    print(f'You will need {no_of_cans} cans of paint')


height = int(input("Height: "))
width = int(input("Width: "))
covarage = 7

paint_calculation(height=height, width=width, cover=covarage)