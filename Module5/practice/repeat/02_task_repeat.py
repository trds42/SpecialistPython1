# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    string = str(number)
    reverse = string[::-1]
    if string == reverse:
        return True
    else:
        return False


n = int(input('n = '))
if palindrome(n):
    print('Yes')
else:
    print('No')
