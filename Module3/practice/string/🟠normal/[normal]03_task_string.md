## "Подсчет подстрок без учета регистра"

### Задание

Подсчитать количество слов «мама»(без учета регистра) во введенной строке.

Т.е. вам подойдут слова и "мама" и "Мама" и "МАМа" и т.д.

### Формат входных данных

Дана произвольная строка.

### Формат выходных данных

Вывести количество найденных слов.

### Решение задачи

```python
text = "Мама мыла раму. Устала мама, но наконец отмыла раму-)"
# TODO: you code here...
string = input('str = ')
string = string.lower()
string = string.replace(',', '')
string = string.replace('.', '')
string = string.replace('-', '')
string = string.replace(')', '')
string = string.replace('(', '')
lst = string.split(' ')
count = 0
for word in lst:
    if word == 'мама':
        count += 1
print(count)
```

---

### Подсказки

<details>
<summary>Подсказка-1</summary>
Преобразуйте исходную строку к нижнему регистру воспользовавшись соответствующим методом.
</details>
