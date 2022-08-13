# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = input('text: ')

if text.count('.') == text.count(','):
    print('Same')
elif text.count('.') > text.count(','):
    print('.')
else:
    print(',')
