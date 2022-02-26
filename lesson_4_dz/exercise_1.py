"""Реализовать структуру данных стэк, который за О(1) выдает минимум в стэке:"""
from collections import deque


class MinStack:
    def __init__(self):
        # основной стек для хранения элементов
        self.stack = deque()
        # вспомогательный стек для хранения минимума элементов
        self.aux = deque()
    # Вставляет заданный элемент поверх стека

    def push(self, val):
        # помещает данный элемент в основной стек
        self.stack.append(val)

    # если вспомогательный стек пуст, помещает в него данный элемент
        if not self.aux:
            self.aux.append(val)
        else:
            # помещает данный элемент во вспомогательный стек
            # если он меньше или равен текущему
            if self.aux[-1] >= val:
                self.aux.append(val)

    # удаляет верхний элемент из стека и возвращает его
    def pop(self):
        if self.isEmpty():
            print("Стек пуст")
            exit(-1)

        # удаляет верхний элемент из основного стека
        top = self.stack.pop()

        # удаляет верхний элемент из основного элемента,
        # если он минимален

        if top == self.aux[-1]:
            self.aux.pop()

        # возвращает удаленный элемент
        return top

    # Возвращает верхний элемент стека
    def top(self):
        return self.stack[-1]

    # Возвращает общее количество элементов в стеке
    def size(self):
        return len(self.stack)

    # возвращает True, если стек пуст; False в противном случае
    def isEmpty(self):
        return not self.stack

    # возвращает минимальный элемент из стека за постоянное время
    def getMin(self):
        if not self.aux:
            print('Стек пуст')
            exit(-1)
        return self.aux[-1]

s = MinStack()

s.push(6)
print(s.getMin())
s.push(4)
s.push(7)
s.push(8)
print(s.getMin())
print(s.isEmpty())
print(s.pop())
print(s.top())
print(s.size())