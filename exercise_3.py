"""4 Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125
...Количество элементов (n) вводится с клавиатуры."""
start = 1
step = -2
stop = int(input('enter number'))
result = 0
while stop != 0:
    result += start
    start = start / step
    stop -= 1

print(f'result = {result}')
