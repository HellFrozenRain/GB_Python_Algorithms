"""2 Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""

number = int(input('enter number'))
even_number = 0
odd_numbers = 0
print(f'number: {number}')
number = abs(number)
while number != 0:
    x = number % 10
    if x % 2 == 0:
        even_number += 1
    else:
        odd_numbers += 1
    number = number // 10
print(f'even number = {even_number}')
print(f'odd numbers = {odd_numbers}')
