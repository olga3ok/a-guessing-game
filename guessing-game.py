import random

print('Добро пожаловать в числовую угадайку!')

limit_min = input('Укажите, в каком диапазоне Вы готовы угадывать числа.\nВведите минимальное в пределах от 1 до 1000: ')
limit_max = input('Введите максимальное число в пределах от 1 до 1000: ')

random_num = random.randint(int(limit_min), int(limit_max) + 1)

def is_valid(s):
    if s.isdigit() and 1 <= int(s) <= 1000:
        return True
    else:
        return False

count_of_attempt = 0

while True:
    number = input(f'Введите целое число от {limit_min} до {limit_max}:   ')
    if not is_valid(number):
        print(f'А может быть все-таки введем целое число от {limit_min} до {limit_max}?')
        continue
    number = int(number)
    if number < random_num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        count_of_attempt += 1
    elif number > random_num:
        print('Ваше число больше загаданного, попробуйте еще разок')
        count_of_attempt += 1
    elif number == random_num:
        print(f'''Вы угадали, поздравляем!
Количество совершённых попыток: {count_of_attempt}''')
        again = input(f'Хотите повторить игру? Да/Нет   ')
        if again == 'Нет':
            break
        else:
            continue

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
