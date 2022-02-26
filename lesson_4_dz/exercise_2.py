"""Написать код для задачи: 'Обработка сетевых пакетов'"""
from collections import deque
size, n = map(int, input().split())

# хранит время окончания обработки пакетов
buffer = deque()

for i in range(n):
    arrival, duration = map(int, input().split())
    # удаляет из буффера пакеты, обработанные к моменту прибытия
    while buffer and buffer[0] <= arrival:
        buffer.popleft()

    if len(buffer) >= size:
        # если буффер переполнен
        print('-1')
    else:
        # если в буффере что то есть
        if buffer:
            # обновляет время прибытия
            arrival = max(arrival, buffer[-1])
        print(arrival)
        # добавляет в очередь текущий пакет
        buffer.append(arrival + duration)
