# Даны номер месяца и номер года. Найдите сколько дней в этом месяце.
# При вводе неверного номера месяца или некорректного значения программа должна сообщить об ошибке
# и попросить ввести корректные данные. Также необходимо учесть високосный или не високосный год.
# Алгоритм проверки на високосный год оформите в виде отдельной функции.
#
# Входная строка содержит два целых числа – номер месяца (возможно, неправильный) и номер года.

def is_leap_year(year) -> bool:
    result = False
    if year % 100 == 0:
        result = year % 400 == 0
    else:
        result = year % 4 == 0
    return result


correct = False
while not correct:
    try:
        inp = input('Month and year: ')
        spl = inp.split(" ")
        month = int(spl[0])
        year = int(spl[1])
        if 0 < month <= 12:
            correct = True
        else:
            print('Первое число должно быть номером месяца')
    except IndexError as ex:
        print('Введите два числа через пробел')
    except ValueError as ex:
        print('Через пробел должны быть введены числа')

if month == 2:
    if is_leap_year(year):
        print(29, "дней")
    else:
        print(28, "дней")
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print(31, "день")
else:
    print(30, "дней")


