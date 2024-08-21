
def longest_palindromic_substring(s):
    def expand_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1: right]

    longest = ""

    for i in range(len(s)):
        long_odd = expand_center(i, i)  # odd
        if len(long_odd) > len(longest):
            longest = long_odd

        long_even = expand_center(i, i+1)  # even
        if len(long_even) > len(longest):
            longest = long_even

    return longest


# Driver Code:
if __name__ == '__main__':
    s = "forgeeekske"
    longest_palindrome = longest_palindromic_substring(s)
    print("Length:", longest_palindrome)

