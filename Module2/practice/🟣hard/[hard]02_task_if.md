## "Шахматы: слон"

### Задание

Требуется определить, бьет ли слон, стоящий на клетке с указанными координатами (номер строки и номер столбца), фигуру, стоящую на другой указанной клетке.

### Формат входных данных

Даны четыре числа целые числа в диапазоне [1, 8], координаты слона и координаты другой фигуры

### Формат выходных данных

Вывести "Да", если слон бьет фигуру или "Нет", если не бьет.

### Решение задачи

```python
# TODO: you code here...
x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))

result = 'No'
i = 1
while i < 8:
    if (x2 == x1 + i or x2 == x1 - i) and (y2 == y1 + i or y2 == y1 - i):
        result = 'Yes'
    i += 1
print(result)
```

---
