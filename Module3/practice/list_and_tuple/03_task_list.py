# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

# TODO: your code here
x = []
n = int(input('n = '))
while n > 0:
    x.append(int(input('Enter number: ')))
    n -= 1
summa = 0
for el in x:
    summa += el
print(summa)
