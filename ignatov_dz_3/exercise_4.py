"""4. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться."""
import random
stop = 100
start = 0

random_array = [random.randint(start, stop) for el in range(10)]
print(random_array)
if random_array[0] > random_array[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0
for i in range(2, 10):
    if random_array[i] < random_array[min1]:
        b = min1
        min1 = i
        if random_array[b] < random_array[min2]:
            min2 = b
    elif random_array[i] < random_array[min2]:
        min2 = i


print(f'the first minimum is {random_array[min1]}')
print(f'the second minimum is {random_array[min2]}')
