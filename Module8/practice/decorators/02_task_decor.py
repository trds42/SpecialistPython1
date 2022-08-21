# Напишите функцию декоратор, которая округляет значение декорируемой функции до двух знаков после  запятой.
# Если округление невозможно, например там строка, или не требуется(целое число) то оставляем результат без изменений.
# Примечание: используйте встроенную функцию round()
def round2(func):
    def wrapper():
        res = func()
        try:
            res2 = round(float(res), 2)
            if res2 % 1 == 0:
                print(res)
            else:
                print(res2)
        except ValueError:
            print(res)
    return wrapper

@round2
def my_function():
    return input("Введите текст: ")

my_function()
