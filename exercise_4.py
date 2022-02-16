"""Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
 выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число."""

number = int(input('enter number'))
total = 0
expression = number * (number + 1) / 2
print(f'n(n+1)/2 = {expression}')
while number != 0:
    total += number
    number -= 1
print(f'1+2+...+n = {total}')
print('Q.E.D.' if total == expression else 'wrong')
