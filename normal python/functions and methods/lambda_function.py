# lambda functions can be written in place of code where a function name would normally go
# Some examples are given of this

# example of something without a lambda function
squares = []
for x in range(1,11):
    squares.append(x**2)

print("Just a for loop")
print(squares)

# same example with a map function (No Lambda)
def square(x):
    return x**2

squares = list(map(square, range(1,11)))

print("Map Function (No Lambda)")
print(squares)

# same example with a map and a lambda function
squares = list(map(lambda x : x**2, range(1,11)))

print("Map function with a lambda")
print(squares)
