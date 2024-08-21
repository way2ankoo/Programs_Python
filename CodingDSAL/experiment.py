dict1 = {
    "ankit": 1,
    "rashmi": 2
}

# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
# print(dict1.pop("ankit", 30))
# print(dict1)


# for i, key in enumerate(dict1.items()):
#     print(i)
#     print(key)


def print_reverse(string):
    reversed_string = ''
    for char in string:
        # print(char)
        reversed_string = char + reversed_string
        # print(reversed_string)
    print(reversed_string)


# Example usage
string = "hello"
# print_reverse(string)

from collections import Counter

def sort_by_moving_duplicates_to_end(arr):
    # Count frequencies of each element
    count = Counter(arr)
    # print(count)

    # Separate unique elements and duplicates
    unique_elements = [key for key in count if count[key] == 1]
    print(unique_elements)
    duplicates = [key for key in count if count[key] > 1]
    print(duplicates)

    # Reconstruct the array
    result = unique_elements + duplicates * 2  # Duplicates should be added in their original frequency

    return result

# Example usage
array = [4, 5, 6, 5, 4, 6, 7, 8, 7, 8, 8]
sorted_array = sort_by_moving_duplicates_to_end(array)
print("Array after sorting:", sorted_array)