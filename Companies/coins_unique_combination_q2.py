def find_combinations(denomination_list, target):
    """
        returns unique combinations which sum to target
        @param:
         denomination_list : (list)array of denominations available
         target : (int)target sum
        @return: list of combination(list)
    """
    def rec(start_idx, ds, target):
        if target == 0:
            result.append(list(ds))
            return

        if target < 0:
            return

        for i in range(start_idx, len(denomination_list)):
            if i > start_idx and denomination_list[i] == denomination_list[i - 1]:
                continue

            ds.append(denomination_list[i])
            rec(i + 1, ds, target - denomination_list[i])
            ds.pop()

    result = []
    rec(0, [], target)
    return result

# def rec(start_idx, ds, result, denominations, target):
#     if target == 0:
#         result.append(ds)
#         return
#
#     if target < 0:
#         return
#
#     for i in range(start_idx, len(denominations)):
#         # handle duplicacy
#         if i > start_idx and denominations[i] == denominations[i-1]:
#             continue
#
#         ds.append(denominations[i])
#         rec(i+1, ds, result, denominations, target-denominations[i])
#         ds.pop()  # backtrack
#
#
# def find_combination(denominations, target):
#
#     result = []
#     rec(0, [], result, denominations, target)
#     return result


if __name__ == "__main__":
    denomination_list = [1, 1, 1, 1, 1, 2, 2, 2, 5, 5]
    target = 12
    combinations = find_combinations(denomination_list, target)
    for combo in combinations:
        print(combo)
