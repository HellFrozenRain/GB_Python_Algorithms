"""Параллельная обработка
По данным n процессорам и m задач определите, для каждой из задач,
каким процессором она будет обработана."""


def swap(i, j):
    processes[i], processes[j] = processes[j], processes[i]


def siftdown(index):
    min_index = index
    l = index * 2 + 1
    if l < n and processes[l] < processes[min_index]:
        min_index = l
    r = index * 2 + 2
    if r < n and processes[r] < processes[min_index]:
        min_index = r
    if index != min_index:
        swap(index, min_index)
        siftdown(min_index)


n, m = map(int, input().split())
processes = [[0, i] for i in range(n)]
tasks = [int(s) for s in input().split()]
current_time = 0
for task_j in tasks:
    current_time = processes[0][0]
    print(processes[0][1], current_time)
    processes[0][0] += task_j
    siftdown(0)
