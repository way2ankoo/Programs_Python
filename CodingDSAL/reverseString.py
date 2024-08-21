def reverse_string(s):
    # Convert string to list of characters for in-place modification
    char_list = list(s)
    start = 0
    end = len(char_list) - 1

    while start < end:
        # Skip spaces from the start
        while start < end and char_list[start] == ' ':
            start += 1

        # Skip spaces from the end
        while start < end and char_list[end] == ' ':
            end -= 1

        # Swap characters if pointers are within bounds
        if start < end:
            # Swap characters at start and end
            char_list[start], char_list[end] = char_list[end], char_list[start]
            start += 1
            end -= 1

    # Convert list back to string
    return ''.join(char_list)


# Example usage
string = "   hello wor  ld  "
reversed_string = reverse_string(string)
print("Reversed string:", reversed_string)
