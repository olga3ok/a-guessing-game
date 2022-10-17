import random
import PySimpleGUI as sg

sg.theme('DarkAmber')

def is_valid(s):
    if s.isdigit() and 1 <= int(s) <= 1000:
        return True
    else:
        return False

sg.popup('Добро пожаловать в числовую угадайку!')

limit_min = int(sg.popup_get_text('Укажите, в каком диапазоне Вы готовы угадывать числа.\nВведите минимальное в пределах от 1 до 1000: '))
limit_max = int(sg.popup_get_text('Введите максимальное число в пределах от 1 до 1000: '))
random_num = random.randint(int(limit_min), int(limit_max) + 1)

count_of_attempt = 1

while True:

    number = sg.popup_get_text(f'Введите целое число от {limit_min} до {limit_max}:   ')
    if not is_valid(number):
        sg.popup(f'А может быть все-таки введем целое число от {limit_min} до {limit_max}?')
        continue
    number = int(number)
    if number < random_num:
        sg.popup('Ваше число меньше загаданного, попробуйте еще разок')
        count_of_attempt += 1
    elif number > random_num:
        sg.popup('Ваше число больше загаданного, попробуйте еще разок')
        count_of_attempt += 1
    elif number == random_num:
        sg.popup(f'''Вы угадали, поздравляем!
Количество совершённых попыток: {count_of_attempt}''')
        again = sg.popup_get_text(f'Хотите повторить игру? Да/Нет   ')
        if again == 'Нет':
            break
        else:
            continue

sg.popup('Спасибо, что играли в числовую угадайку. Еще увидимся...')