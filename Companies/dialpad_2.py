# given an array of integers, find all subsequences having length 3 and sum of 3 elements = sum and all three elements
# are distinct


def find_subsequences(arr, sum):
    preprocessed_dict = {}
    for e in arr:
        if e not in preprocessed_dict:
            preprocessed_dict[e] = 1
        else:
            preprocessed_dict[e] += 1

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            k = sum - arr[i] - arr[j]
            if arr[i] != arr[j] and arr[j] != k and arr[i] != k:
                if k in preprocessed_dict:
                    print(f"{arr[i]}, {arr[j]}, {k}")







#####code review####

# Functionality: Verify it correctly identifies unique triplets
# Edge case: array less than 3 elements, array with all identical elements, or all negative numbers
# Efficiency : time complexity O(n^2), space complexity : dictionary
# Readability & Maintainability : proper variable names, documentation, comments, proper function name
# Error handling : not list input or non integer elements
# Code Stype : proper indentation, spacing, and line length
# duplicate output

def find_unique_triplets(arr, target_sum):
    """
    Find and print all unique triplets in the array that sum up tp target_sum
    :param Arr: list :  input integer list
    :param target_sum: int : target sum of triplets
    """
    if not isinstance(arr, list):
        raise TypeError(" Input should be a list of integers")
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements in the array should be integers")
    if len(arr) < 3:
        raise ValueError("Input array must contain atleast 3 elements")

    # dictionary to count occurrences of each element in the array
    element_count = {}
    for element in arr:
        element_count[element] = element_count.get(element, 0) + 1

    # set to keep track of printed triplets to avoid duplication
    seen_triplets = set()

    # iterate over all pairs of elements in the array
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            first_element, second_element = arr[i], arr[j]
            third_element = target_sum - first_element - second_element
            if first_element != second_element and second_element != third_element and first_element != third_element:
                # check if third element exists in dictionary
                if third_element in element_count:
                    # Create a sorted tuple of the triplet to avoid duplicates
                    triplet = tuple(sorted((first_element, second_element, third_element)))
                    # print(triplet)
                    if triplet not in seen_triplets:
                        seen_triplets.add(triplet)
                        print(f"{triplet[0]}, {triplet[1]}, {triplet[2]}")


arr = [1, 4, 2, 3, 2, 5]
sum = 8
# find_subsequences(arr, sum)
find_unique_triplets(arr, target_sum=sum)
