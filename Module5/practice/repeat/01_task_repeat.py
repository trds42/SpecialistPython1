# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random


def gen_list(size, of, to):
    lst = []
    for i in range(size):
        lst.append(random.randint(of, to))
    return lst


def gen_list2(size, of, to):
    lst = [random.randit(of, to) for _ in range(size)]


n = int(input('n = '))
a = int(input('a = '))
b = int(input('b = '))
lst = gen_list(n, a, b)
print(lst)

