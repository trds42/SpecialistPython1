# Напишите функцию принимающую общее количество объектов(например, товаров)
# которые нужно отобразить и количество объектов, которые нужно отобразить на каждой странице.
# Функция должна вычислять количество страниц для отображения всех объектов.

# Под пагинацией понимают показ ограниченной части информации на одной
# веб-странице и вывода списка остальных страниц.

import math


def pagination(num_items, items_on_page):
    return math.ceil(num_items / items_on_page)


items = int(input('items = '))
items_on_page = int(input('items on page = '))

print('number of pages =', pagination(items, items_on_page))

