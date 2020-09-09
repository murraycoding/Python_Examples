# The range function is a function which generates a sequence of numbers used for looping

# one parameter give = prints from 0 to n (not including n)
print("One parameter range")
x = range(10)
for num in x:
    print(num)

# two parameters given = prints from the starting number to the ending number (not including the end number)
print("Two parameter range")
x = range(2,8)
for num in x:
    print(num)

# three parameters given = prints from start to end (not including end) but incremeting by the 3rd parameter
print("Three parameter range")
x = range(3,20,2)
for num in x:
    print(num)