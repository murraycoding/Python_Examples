def exp(n):
    n = 2
    def num(x):
        nonlocal n
        return x**n
    return num

square = exp(5)

print(square(9))
