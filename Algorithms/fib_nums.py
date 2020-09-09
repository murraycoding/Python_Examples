# function to find the nth fibonacci number

def fib_num(n):
    # returns 1 if the function is looking for the first two numbers
    if n == 1 or n == 2:
        return 1
    # the function will return the sum of the two numbers before it in the sequence
    else:
        return fib_num(n-2) + fib_num(n-1)

print(fib_num(8)) # Result = 21
