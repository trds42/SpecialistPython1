## "Какая длиннее"

### Задание

Даны две строки. Выведите ту, в которой больше символов. \
Если символов одинаково, выведите любую.

### Формат входных данных

Даны две произвольные строки.

### Формат выходных данных

Вывести наиболее длинную или любую, если длина строк одинаковая.

### Решение задачи

```python
string1 = input("Первая строка:")
string2 = input("Вторая строка:")
if len(string1) >= len(string2):
    print(string1)
else:
    print(string2)
```

---

### Данные для самопроверки

| string1 | string2 |Результат |
| :---: | :---: | :---: |
| hello |   hi  | hello |
| name |   surname  | surname |
| текст |  кокос   | кокос |


### Подсказки

<details>
<summary>Подсказка-1</summary>
Вспомните про функцию len()
</details>
