# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"
text = input('text: ')

i = 0
start = 0
end = 0
if text[0] == 'б':
    for i in range(len(text)):
        if text[i] == ' ':
            end = i
            break
else:
    for i in range(len(text)):
        if text[i] == ' ':
            if text[i+1] == 'б':
                start = i+1
                break
    if start != 0:
        for i in range(start, len(text)):
            if text[i] == ' ':
                end = i
                break
if end == 0:
    print('No words with "б"')
else:
    print(text[start:end])
