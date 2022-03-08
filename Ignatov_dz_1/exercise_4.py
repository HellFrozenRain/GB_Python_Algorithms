"""Написать программу, которая генерирует в указанных пользователем границах
случайное целое число,
случайное вещественное число,
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
 Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно."""
import random


def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

print('для получения диапазона границы должны быть одного типа')
left_border = input('введите левую границу целых чисел')
right_border = input('введите правую границу целых чисел')
if left_border.isdigit() == True and right_border.isdigit() == True:
    print(random.randrange(int(left_border), int(right_border) + 1))
else:
    print('вы ввели не число')
left_border = input('введите левую границу вещественных чисел')
right_border = input('введите правую границу вещественных чисел')
if is_float(left_border) == True and is_float(right_border) == True:
    print(random.uniform(float(left_border), float(right_border) + 1))
else:
    print('вы ввели не число')
left_border = input('введите левую границу символов')
right_border = input('введите правую границу символов')
if left_border.isalpha() == True and right_border.isalpha() == True:
    x = ord(left_border.lower())
    y = ord(right_border.lower())
    z = random.randrange(x, y + 1)
    print(chr(z))
else:
    print('вы ввели не символ')