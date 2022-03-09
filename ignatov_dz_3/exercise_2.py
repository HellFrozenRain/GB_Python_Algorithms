"""В массиве случайных целых чисел поменять местами минимальный
и максимальный элементы."""

import random
max_number = 0
min_number = 100
random_array = [random.randint(max_number, min_number) for el in range(10)]
print(random_array)
for el in random_array:
    if el > max_number:
        max_number = el
    if el < min_number:
        min_number = el
print(f'maximum number is {max_number}')
print(f'minimum number is {min_number}')
print(f'index of maximum number is {random_array.index(max_number)}')
print(f'index of minimum number is {random_array.index(min_number)}')
a = random_array.index(max_number)
b = random_array.index(min_number)
random_array[a], random_array[b] = random_array[b], random_array[a]
print(random_array)
