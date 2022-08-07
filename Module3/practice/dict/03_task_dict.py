# Данные о сотрудниках в программе хранятся в словаре
staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 47800
    },
]
# Вычислите:
print("Имя и Фамилию сотрудника с самой высокой зарплатой:")

# TODO: your code here
max_salary = {
        'name': '',
        'surname': '',
        'salary': 0
    }
for person in staff:
    if person['salary'] > max_salary['salary']:
        max_salary['salary'] = person['salary']
        max_salary['name'] = person['name']
        max_salary['surname'] = person['surname']
print(max_salary['name'], max_salary['surname'])

print("Имя и Фамилию сотрудника с самой низкой зарплатой:")

# TODO: your code here
min = staff[0]['salary']
index = 0
for i in range(len(staff)):
    if staff[i]['salary'] < min:
        min = staff[i]['salary']
        index = i
print(staff[index]['name'], staff[index]['surname'])

print("Среднеарифметическую зарплату всех сотрудников")

# TODO: your code here
count = 0
summa = 0
for person in staff:
    summa += person['salary']
    count += 1
print(summa / count)

print("Количество однофамильцев в организации")

# TODO: your code here
count = 0
for person in staff:
    surname = person['surname']
    match_count = 0
    for another_person in staff:
        if another_person['surname'] == surname:
            match_count += 1
    if match_count > 1:
        count += 1
print(count)

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")

# TODO: your code here
staff = sorted(staff, key=lambda x: x['salary'])
for person in staff:
    print(person['name'], person['surname'])
