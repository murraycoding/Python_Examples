# Notes on the walrus operator introduced in Python 3.8

# This is the basic case, using the operator inside of a print function

# No Walrus operator
walrus_var = True
print(walrus_var)

# With Walrus operator
print(walrus_var := True)

# This is just an example of a more advanced way to use the walrus operator

# No Walrus operator
num_list = []
number = input("What is your number? ")
while number > 5:
    num_list.append(number)
    number = input("What is your number? ")

# With Walrus Operator
num_list = []
while number := input("What is your number? ") > 5:
    num_list.append(number)