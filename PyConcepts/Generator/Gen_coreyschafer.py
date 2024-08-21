# normal square function
# def square_numbers(nums):
#     sq = []
#     for i in nums:
#         sq.append(i * i)
#     return sq

# generator function :generate value on the fly
def square_numbers(nums):
    for i in nums:
        yield i * i


my_nums = square_numbers([1, 2, 3, 4, 5])  # generator object

# my_nums = [x * x for x in [1, 2, 3, 4, 5]]  # list comprehension
# my_nums = (x * x for x in [1, 2, 3, 4, 5])  # generator expression
print(my_nums)

print(next(my_nums))
print(next(my_nums))

# for num in my_nums:
#     print(num)
