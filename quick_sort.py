def hoar_sort(arr):
    if len(arr) <= 1:
        return arr
    elem = arr[0]
    left = list(filter(lambda x: x < elem, arr))
    mid = [i for i in arr if i == elem]
    right = list(filter(lambda x: x > elem, arr))
    return hoar_sort(left) + mid + hoar_sort(right)


array = [9, 8, 7, 6, 5]
print(hoar_sort(array))
