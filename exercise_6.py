"""Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр."""

number_a = int(input('enter number A'))
number_b = int(input('enter number B'))
number_c = int(input('enter number C'))


def total(n):
    if n == 0:
        return 0
    return n % 10 + total(n // 10)


total_a = total(number_a)
total_b = total(number_b)
total_c = total(number_c)
if total_c >= total_b and total_c >= total_a:
    print(f'sum of digits is: {total_c}')
    print(f'maximum number: {number_c}')
elif total_b >= total_c and total_b >= total_a:
    print(f'sum of digits is: {total_b}')
    print(f'maximum number: {number_b}')
else:
    print(f'sum of digits is: {total_a}')
    print(f'maximum number: {number_a}')
