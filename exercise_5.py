"""Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры."""

digits_array = input('enter digits')
digit = input('enter digit')
result = 0
for el in digits_array:
    if digit in el:
        result += 1
print(f'the amount of digit {digit} is {result}')