## "Проверка пароля"

### Задание

Для повышения безопасности, пароли пользователей должны соответствовать требованиям. \
Проверьте, соответствует ли данный пароль предложенным требованиям.

Требования к паролю:
* Минимум 6 символов
* Должен содержать спецсимвол "#"
* Должен начинаться с большой буквы

### Формат входных данных

Дана строка, пароль пользователя.

### Формат выходных данных

Вывести "безопасный", если строка пароля соответствует требованиям безопасности или "не безопасный" в противоположном случае.

### Решение задачи

```python
password = input("Enter password: ")
# TODO: you code here...
string = input('str = ')
strong = 'No'
if len(string) >= 6:
    if string[0].isupper():
        if '#' in string:
            strong = 'Yes'
print(strong)
```

---

### Данные для самопроверки

| Дано | Результат |
| :---: | --- |
|    a12345   | не безопасный |
|    F12#34    | безопасный  |
|    F12$3    | не безопасный |
|    #Derpassword    | не безопасный |
|    Derpassword#    | безопасный |

### Подсказки

<details>
<summary>Подсказка-1</summary>
Для проверки "начинается ли строка с большой буквы", есть готовый метод.
</details>

<details>
<summary>Подсказка-2</summary>
Для проверки "есть ли в строке символ", воспользуйтесь оператором вхождения in

```python
"h" in "hello"  # True
```

```python
"b" in "hello"  # False
```
</details>
