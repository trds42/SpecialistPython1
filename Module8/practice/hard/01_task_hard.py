# "Банкомат"
# В банкомате есть купюры 5000, 2000, 1000 и 500 рублей.
# Напишите функцию, которая будет рассчитывать количество купюр, которыми можно будет выдать
# запрошенную пользователем сумму и возвращать ее в виде словаря, ключами в котором будут номиналы банкнот,
# а значениями кол-во банкнот. Если пользователь запросил некорректную сумму,
# нужно вывести дружественное сообщение об ошибке.
# Результат работы программы - текстовый отчет о номиналах и количестве купюр.
snake_input = int(input('Summa = '))
snake_n = snake_input
result = {key: 0 for key in [5000, 2000, 1000, 500]}
for banknote, count in result.items():
    if snake_n >= banknote:
        count = snake_n // banknote
        result[banknote] = count
        snake_n -= banknote * count
if snake_n > 0:
    print(f"Please input a sum kratnoe 500. We don't have {snake_n} rubles.")
else:
    print(result)
    with open("result.txt", "w", encoding="UTF-8") as log:
        log.write(f"For {snake_input} rubles you get:\n")
        for banknote, count in result.items():
            log.write(f"{count} of {banknote} banknotes\n")
