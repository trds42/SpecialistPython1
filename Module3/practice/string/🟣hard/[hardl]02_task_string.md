## "Подсчет длинных слов"

### Задание

Даны две строки s1 и s2. Определите, можно ли составить строку s2, используя только символы из строки s1 (каждую букву можно использовать только один раз).

### Формат входных данных

Даны две строки.

### Формат выходных данных

Вывести "Да", если из символов строки s1 можно составить строку s2 и "Нет", если нельзя.

### Решение задачи

```python
# TODO: you code here...
s1 = 'hello my name is Boris'
s2 = 'ih'
data1 = set(s1)
data2 = set(s2)
result = data1.intersection(data2)
if data2 == result:
    print('yes')
else:
    print('no')
```

---

