from random import randint

arr_non_sorted = [randint(0, 100) for _ in range(100)]
sort = list(set(arr_non_sorted))
print(sort)


def linear_search(arr, elem):
    for i in range(len(arr)):
        if arr[i] == elem:
            return i
    return -1


def binary_search(arr, item):
    start = 0
    stop = len(arr) - 1
    while start <= stop:
        midpoint = (start + stop) // 2
        guess = arr[midpoint]
        if guess == item:
            return midpoint
        if guess > item:
            stop = midpoint - 1
        else:
            start = midpoint + 1
    return


n = 2
print(n)

res = binary_search(sort, n)
print(f"Result: {'found' if res else 'not found'}")
