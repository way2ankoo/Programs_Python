# Given a string “abchelloabctesthello”, find all sequences that have 3 or more characters matching and print them
# o/p : abc, hel, hell, hello


def find_repeated_sequences(s, min_length=3):
    n = len(s)
    if n < min_length:
        return
    seen = {}
    result = set()

    # Check all substrings with lengths from min_length to n
    for length in range(min_length, n + 1):
        # print("for length: ", length)
        for i in range(n - length + 1):
            # print("i is : ", i)
            substring = s[i:i + length]
            # print(substring)
            if substring in seen:
                # result.add(substring)
                print(substring)
            else:
                seen[substring] = i
            # print(seen)
            # print(result)

    # return sorted(result)

def find_repeated_sequences1(s, min_length=3):
    n = len(s)
    if n < min_length:
        return

    # seen = set()
    repeated = set()

    for length in range(min_length, n + 1):
        current_set = set()
        for i in range(n - length + 1):
            substring = s[i:i + length]
            if substring in current_set:
                repeated.add(substring)
            else:
                current_set.add(substring)
        # seen.update(current_set)

    for seq in repeated:
        print(seq)


# Example usage
string = "abchelloabctesthello"
find_repeated_sequences(string)
# find_repeated_sequences1(string)
# print("Repeated sequences with 3 or more characters are:", sequences)