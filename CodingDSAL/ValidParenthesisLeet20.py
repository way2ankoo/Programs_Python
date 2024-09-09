def is_matching(a, b):
    return (a == '(' and b == ')') or (a == '{' and b == '}') or (a == '[' and b == ']')


def isValid(s: str) -> bool:
    stack = []
    for c in s:
        if c in ['(', '[', '{']:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            elif not is_matching(stack[-1], c):
                return False
            else:
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


print(isValid('{()}['))
