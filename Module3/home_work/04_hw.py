# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]

numbers = [2, -5, 8, 9, -25, 25, 4]
squares = []
for number in numbers:
    if number > 0:
        square = number**0.5
        if square % 1 == 0:
            squares.append(int(square))
print(squares)
