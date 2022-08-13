# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
max_length = 0
max_length_name = ''
for name in names:
    length = len(name)
    if length > max_length:
        max_length = length
        max_length_name = name
print(max_length_name)
