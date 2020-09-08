# an example of all of the types of loops in python

# while loop
print("While loop example")
x = 0

while x < 10:
    print(x)
    x += 1

# for loop example 1
print("For Loop Example 1")
contacts = ['Brian','Ed','Joe','Kyle']

for contact in contacts:
    print(contact)

# for loop example 2
print("for loop example 2")

for index, contact in enumerate(contacts):
    print(f'Contact {index+1}: {contact}')

# for loop example 3
print("for loop example 3")

for index in range(len(contacts)):
    print(f'Contact {index+1}: {contacts[index]}')
