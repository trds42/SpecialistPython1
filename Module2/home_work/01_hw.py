# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Формат входных данных
# Вводятся 3 натуральных числа n, m и k. Точно известно, что  k ≠ n ⋅ m.
# Формат выходных данных
# Выведите «YES», если можно отломить от шоколадки ровно k долек, и «NO» иначе.

# TODO: your code here
n = int(input('n = '))
m = int(input('m = '))
k = int(input('k = '))

result = 'NO'

i = 1
while i < n:
    if k == m * i:
        result = 'YES'
        break
    i += 1

j = 1
while j < m:
    if k == n * j:
        result = 'YES'
        break
    j += 1

print(result)
