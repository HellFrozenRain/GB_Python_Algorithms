"""3 Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843."""


def reverse_order(n):
    if n < 10:
        return n
    temp = n
    digits = 0
    while temp > 9:
        temp = temp // 10
        digits += 1
    return (n % 10) * (10 ** digits) + reverse_order(n // 10)


print(reverse_order(int(input('enter number'))))
