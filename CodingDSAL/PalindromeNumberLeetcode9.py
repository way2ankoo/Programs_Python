def is_palindrome(number: int) -> bool:
    original_number = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    return original_number == reversed_number


assert is_palindrome(123) == True, "Not a palindrome number"
