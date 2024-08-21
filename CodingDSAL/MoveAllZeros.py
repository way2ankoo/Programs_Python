def move_zeros_to_right(arr):
    n = len(arr)
    i = 0
    for j in range(n):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return arr


def move_zeros_to_left(arr):
    n = len(arr)
    i = n - 1
    for j in range(n - 1, -1, -1):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i -= 1
    return arr


array = [1, 0, 2, 0, 0, 12]
move_zeros_to_right(array)
print("Array after moving zeros to left:", array)

move_zeros_to_left(array)
print("Array after moving zeros to left:", array)
