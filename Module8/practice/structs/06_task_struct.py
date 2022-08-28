# Вы написали программу для работы с сотрудниками и вам ее необходимо протестировать.
# Для теста нужны большие списки сотрудников (100+).
# Вбивать вручную столько данных займет очень много времени.
# Напишите программу, генерирующую списки сотрудников со следующими параметрами:
# 1. Имя
# 2. Фамилия
# 3. Возраст
# 4. Профессия
# 5. Зарплата
# Примечание: Данные сгенерированных сотрудников могут повторяться

import random

names = ['Boris', 'Ilya', 'Vera', 'Irina']
surnames = ['Kazakov', 'Petrov', 'Usakov']
professions = ['Builder', 'Programmer', 'Manager']
result = []
for i in range(100):
    current_worker = {'Name': random.choice(names), 'Surname': random.choice(surnames),
                      'Age': random.randint(5, 80), 'Profession': random.choice(professions),
                      'Salary': random.randint(0, 100000000)}
    result.append(current_worker)
print(result)
