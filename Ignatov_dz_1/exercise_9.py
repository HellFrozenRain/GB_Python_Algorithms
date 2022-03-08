# Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('enter number a'))
b = int(input('enter number b'))
c = int(input('enter number c'))
if c > a > b or c < a < b :
    print(f'average number: a = {a}')
elif a > b > c or a < b < c:
    print(f'average number: b = {b}')
elif b > c > a or b < c < a:
    print(f'average number: c = {c}')
else:
    print('enter three different numbers')