def fib(num):
    # return n-th Fibonacci number
    if num == 1 or num == 2:
        return 1
    
    return fib(num-1)+fib(num-2)


# print(fib(6))
