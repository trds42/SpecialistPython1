# Посчитайте количество согласных букв в данной строке.

text = input('text: ')

count = 0
for el in text:
    if el not in ['а', 'у', 'о', 'и', 'э', 'ы', 'я', 'ю', 'е', 'ё']:
        count += 1
print(count)
