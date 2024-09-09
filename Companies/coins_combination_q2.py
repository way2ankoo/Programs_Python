def get_combinations(idx, ds, input_list, target):
    """
    prints all combinations which sum to target
    @param:
     ls : (list)array of denominations available
     target : (int)target sum
    """
    if target == 0:
        print(ds)
        return

    # base case
    if idx >= len(input_list) or target < 0:
        return

    # pick case
    ds.append(input_list[idx])
    get_combinations(idx + 1, ds, input_list, target-input_list[idx])
    ds.pop()

    # not pick case
    get_combinations(idx + 1, ds, input_list, target)


if __name__ == "__main__":
    input_list = [1, 1, 1, 1, 1, 2, 2, 2, 5, 5]
    target = 12
    set_c = set()
    get_combinations(0, [], input_list, target)
