## "Трехзначное ли"

### Задание

Проверьте, является ли данное число трехзначным.

### Формат входных данных

Дано целое число.

### Формат выходных данных

Вывести "Да", если данное число трехзначное и "Нет" в противоположном случае.

### Решение задачи

```python
# TODO: you code here...
n = int(input('n = '))

if 100 <= n <= 999 or -100 >= n >= -999:
    print('Yes')
else:
    print('No')
```

---
