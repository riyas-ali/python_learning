def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d


result1, result2 = add_sub(6, 4)
print(result1)
print(result2)


def person(name, age=18):
    print(name)
    print(age)


person('riyas', 15)
person(age=15, name='ashiq')
person('uwais')


def sum_of(*b):
    c = 0
    for i in b:
        c = c + i
    print(c)


sum_of(5, 34, 53, 65)