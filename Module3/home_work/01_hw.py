# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
length = len(names)
for i in range(length):
    if i == length - 1:
        print(names[i])
    else:
        print(names[i], end=', ')
        
# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр
