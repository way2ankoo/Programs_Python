# find max length substring of repeated characters
# i/p : abdcebbbccccab
# op : cccc

def find_max_length_substring(input_string):
    n = len(input_string)
    # print(n)
    if input_string is None or n == 0:
        return ""

    max_len = 1
    current_len = 1
    max_char = input_string[0]

    for i in range(1, n):
        # print(i)
        if input_string[i] == input_string[i-1]:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
                max_char = input_string[i-1]
            current_len = 1

    # last substring check
    if current_len > max_len:
        max_len = current_len
        max_char = input_string[len(input_string) - 1]
    print(max_char)
    print("ans: ", max_len)

    max_len_str = ""
    for i in range(max_len):
        max_len_str += max_char

    print(max_len_str)


str = "abdcebbbccccddd"
find_max_length_substring(str)