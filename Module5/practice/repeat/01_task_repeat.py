# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random


def gen_list(size, of, to):
    lst = []
    for i in range(size):
        lst.append(random.randint(of, to+1))
    return lst


n = int(input('n = '))
a = int(input('a = '))
b = int(input('b = '))
lst = gen_list(n, a, b)
print(lst)

