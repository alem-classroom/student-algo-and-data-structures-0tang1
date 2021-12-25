def fib(num):
    # return n-th Fibonacci number
    n1 = 0
    n2 = 1
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        for i in range(1, num):
            n = n1 + n2
            n1 = n2
            n2 = n
        return n2


# print(fib(6))
