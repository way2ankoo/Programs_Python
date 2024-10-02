def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fib_dp(n, memo):
    if memo[n] == -1:
        # res = 0
        if n == 0 or n == 1:
            res = n
        else:
            res = fib(n - 1) + fib(n - 2)
        memo[n] = res
    return memo[n]


def fibo_tabu(n):
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]


def fib_itr(n):
    if n == 0 or n == 1:
        return n

    a, b = 0, 1

    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
    return b


if __name__ == "__main__":
    # 0, 1, 1, 2, 3, 5, 8, 13, 21
    n = 7
    print(fib(n))
    print(fib_itr(n))

    # memo = [-1 for _ in range(n + 1)]
    memo = [-1] * (n+1)
    print(memo)
    print(fib_dp(n, memo))
    print(fibo_tabu(n))
