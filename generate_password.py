import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

count_of_passwords = input('Укажите количество паролей для генерации:  ')
length_of_password = input('Укажите длину одного пароля:   ')
digits_on = input('Включать ли цифры 0123456789? (y/n)   ')
uppercase_on = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)   ')
lowercase_on = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?   ')
punctuation_on = input('Включать ли символы !#$%&*+-=?@^_? (y/n)   ')
exc_on = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)   ')

if digits_on.lower() == 'y':
    chars += digits
if uppercase_on.lower() == 'y':
    chars += uppercase_letters
if lowercase_on.lower() == 'y':
    chars += lowercase_letters
if punctuation.lower() == 'y':
    chars += punctuation
if exc_on.lower() == 'y':
    for c in 'il1Lo0O':
        chars.replace(c, '')

def generate_password(length, chars):
    password = ''
    for i in range(int(length)):
        password += random.choice(chars)
    return password

for _ in range(int(count_of_passwords)):
    print(generate_password(length_of_password, chars))
