# Дан прямоугольник размером n×m. Напишите программу, вычисляющую, сколько квадратов
# со стороной m от него получится отрезать.

# На вход программе подается строка формата nxm (x - латинская буква икс).
# Пример входных данных: 12x6
# Если данные вводятся в неверном формате, сообщить об этом и запросить ввод заново.

def getdata():
    str = input('nxm: ')
    spl = str.split("x")
    try:
        n = int(spl[0])
        m = int(spl[1])
        return n, m
    except IndexError as ex:
        print("Разделите цифры буквой x")
        return getdata()
    except ValueError as ex:
        print("Введите цифры, разделенные буквой x")
        return getdata()
    except BaseException as ex:
        print("Неверные данные, введите еще раз")
        return getdata()


n, m = getdata()
print(n // m)
