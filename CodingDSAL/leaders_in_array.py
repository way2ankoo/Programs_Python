def find_leaders(arr):
    n = len(arr)
    max_e = arr[-1]
    leaders = [max_e]

    # traverse
    for e in arr[n-2::-1]:
        if e > max_e:
            max_e = e
            leaders.append(max_e)
    leaders.reverse()
    return leaders


array = [16, 17, 4, 3, 5, 2]
leaders = find_leaders(array)
print(leaders)
