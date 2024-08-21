def longest_symmetric(string):
    start = mid = last_gt = end = 0
    best = 0
    while start < len(string):
        current = min(mid - start, end - mid)
        if best < current:
            best = current

        if end - mid == current and end < len(string):
            if string[end] == '?':
                end += 1
            elif string[end] == '>':
                end += 1
                last_gt = end
            else:
                end += 1
                mid = end
                start = max(start, last_gt)
        elif mid < len(string) and string[mid] == '?':
            mid += 1
        elif start < mid:
            start += 1
        else:
            start = max(start, last_gt)
            mid = mid + 1
            end = max(mid, end)

    return 2 * best


for s in ('<<?',):
    print(s, longest_symmetric(s))

# Test cases
print(longest_symmetric("<><??>>"))   # Output: 4
print(longest_symmetric("??????"))    # Output: 6
print(longest_symmetric("<<?"))       # Output: 2
