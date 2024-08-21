# learning lambda functions : anonymous one liner function
from functools import reduce

# simple add function
add_1 = lambda x, y: x + y
print(add_1)
# result = add_1(3, 7)
# print(result)

# lambda usage in map function : changes the values
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sq = list(map(lambda x: x ** 2, range(10, 0, -1)))
print(sq)

# filter : filters the values
ev = list(filter(lambda x: x % 2 == 0, nums))
print(ev)

# sorted
values = [(1, 'b', "Hello"), (2, 'a', "world"), (3, 'c', "ok")]

sorted_values = sorted(values, key=lambda x: x[1] + x[2])
print(sorted_values)

# reduce : reduces iterable to single value

sum_nums = reduce(lambda acc, x: acc + x, nums)
print(sum_nums)

max_value = reduce(lambda max_element, x: max_element if max_element > x else x, nums)
print(max_value)

# some fancy computation
fancy = {x: (lambda x: x * x)(x) for x in range(5)}
print(fancy)
