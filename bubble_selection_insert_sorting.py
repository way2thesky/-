from random import randint
from copy import copy

# Алгоритм выполняет итерации по списку, сравнивая элементы попарно и меняя их местами.
def bubble_sort(arr):
    last_item = len(arr) - 1
    for run in range(0, last_item):
        for x in range(0, last_item - run):
            if arr[x] > arr[x + 1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]

    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


def insert_sort(arr):
    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > item_to_insert:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item_to_insert
    return arr


# O(n^2)
h1 = [randint(0, 10) for _ in range(100)]
h2 = copy(h1)
h3 = copy(h1)
h4 = copy(h1)
print(h1)
print(bubble_sort(h1))

print(h2)
print(selection_sort(h2))

print(h3)
print(insert_sort(h3))
