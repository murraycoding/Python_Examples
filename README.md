# Python Notes
folder_name = Regular Python
This will be where all notes will be regarding things which are normally in Python (not including the standard library you can import from). If any importing needs to happen in order to use a particular feature, please refer to the notes on Python Libraries later in the notes.

## Basics
All of the basics of Python. Things to know just to get started writing a simple program

### The print method
The print statement is one of the most fundamental things in Python. This can be used for debugging, writing things to a command line and many others. 

### Interactive Mode

You can use python without executing a prewritten program or script. In order to simply type python commands, in the command line type 'python'. Depending on the system path on your computer, this may be different (possibly 'python3'). Press enter after typing 'python' to enter 'interactive mode'. In this mode, you can pass any python commands you would if it were a regular python function. In the example below, I used PowerShell to write a small program to showcase interactive mode. The '>>>' symbol represents the *primary prompt*. The '...' represents the *secondard prompt*.

    PS C:\Users\bmurr> python
    Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> x = 5
    >>> if x = 4:
    ...     print('x is equal to 4')
    ... else:
    ...     print('x is not equal to 4')
    x is not equal to 4

### Data Types

#### Numbers

#### Strings

#### Booleans


## Contol flow

### If Statements

Here is an example of an if statement.

    def example_function():
        x = 5

        if x > 4:
            print(f"{x} is greater than 4")
        else:
            print(f"{x} is not greater than 4")

This is an example of an else if statement.

    def example_function():
        x = 5

        if x > 10:
            print(f"{x} is greater than 10")
        elif x > 4:
            print(f"{x} os greater than 4 and less than or equal to 10.")
    
### For Loops (example done)

In Python, for loops are handled a bit different than they are in any other language. Here is the standard for loop interating over a list. In the example below, a list is defined named 'nums' and I will loop through the nums list and print it out. Notice is this for loop the index references the object itself. 

    def for_loop_example():

### While Loops (example done)
In a while loop, the loop is continuously run until a certain condition is not met. If an index is being used, it is important to increment or decrement the index to prevent an infinite loop from occuring.

### Break/Continue Statemetns and Else in loops

### pass Statements

## Functions/Methods

A function is a basic concept in all conputer science. A function, in general, is something which takes a set of parameters, does something to them and then returns an output. It is considered good practice to not alter or edit the input variables. For example, the two functions below both do the same thing. In function_one the a variable is changed and in function_two, neither a or b is changed.
    
    # altering the value of a is considered a bad practice
    def function_one(a,b):
        a = a + b # finds the sum and sets it equal to a
        return a
    
    # not altering the values of the input arguments is considered a good practice
    def function_two(a,b):
        return a + b # returns the sum
        
If no return statement is given, or if there is no value to return in the given return statement, Python will always return "None" to the command line. This is the same with class methods (which are just functions inside of classes - for more on this see the class section of these notes).

### The Range Function (example done)
The range function will produce a sequence of integers to loop over. The function can either take one, two or three parameters. Please see the example in the repo for more infroamtion. In the notes is included the example with three parameters.

    # three parameters given = prints from start to end (not including end) but incremeting by the 3rd parameter
    print("Three parameter range")
    x = range(3,20,2)
    for num in x:
        print(num)

### List Methods

#### Append (example done)
Append is probably the most common list method in many languages. In Javascript, for example, it is called 'push'. This method adds one or more elements to the end of an already existing list. If the original list is empty, whatever is added becomes the list itself. See the example below for how the append method works.

    arr1 = ["one","two","three","four"]
    arr1.append("five")
    
    print(arr1) # Result = ["one","two","three","four","five"]

#### The Zip Function (example done)

The zip function takes two or more interables of any size. The function will return a zip object, which is an interable of tuples. Each tuple in the interable will have one element from each of the iterables passed into the zip function (The function takes the element in order, i.e. The first tuple will be all of the first elements of the iterables, the second tuple will be all of the second elements in the iterables). Keep in mind that the number of elements in each tuple will be the number of iterables passed to the zip function in the first place and the number of tuples as a result of the zip function will be the length of the shortes iterable of the iterables passed to the zip function. 

    arr1 = ["One","Three","Five"]
    arr2 = ["Two","Four","Six","Seven"]

    zipped = zip(arr1, arr2)

    for x in zipped:
        print(x)

    # Result
    ("One","Two")
    ("Three", "Four")
    ("Five", "Six")

Notice the result did not print out "Seven". This is because the zip function only will contain n elements where n is the length of the shortest iterable. In this case, the length of arr1 is 3 and the length of arr2 is 4 so the result of the zip function contains 3 elements. This is just to ensure if can successfully take one element from each iterable.

There are other ways to use the zip function. See the for loops below for two examples of this.

    arr1 = ["One","Three","Five"]
    arr2 = ["Two","Four","Six","Seven"]

    # accessing the items in the for loop directly
    for item in zip(arr1, arr2):
        print item

    # Result
    ("One","Two")
    ("Three", "Four")
    ("Five", "Six")

    #accessing each of the separate items in the tuples
    for a, b in zip(arr1, arr2)
        print f"{a} and {b}"

    # Result
    One and Two
    Three and Four
    Five and Six


### Lambda Functions (example done)

Often times you are required to include a function as an argument in another function. The classic example is the map function. In the map function takes two parameters.

1. The function to run each element through
2. The iterable full of the elements to be run through the function

You can pass any number of iterables in a number of different formats (list, tuple, etc.) in the second parameter.

There are three examples below. The first is an example of generating a list of the first 10 square numbers using a for loop (all of the examples will have the same output, they will just be shown in different methods). The second method will use a map function and a separate square function to square the numbers. The last example will use the same map function, but it will use a lambda function to square the numbers.

    # Example 1: For Loop

    squares = []

    for x in range(1,11):
        squares.append(x**2)
    
    # Example 2: Map Function - No Lambda
    def square(x):
        return x**2

    squares = list(map(square, range(1,11)))

    # Example 3: Map Function - With Lambda

    squares = list(map(lambda x : x**2, range(1,11)))
    
### Decorators (general example done)

#### What is a decorator?
A decorator is a function which wraps around another function. It essentially provides extra functionality to an already existing function. With a decorator, you can write it once and apply it to as many other functions as you would like. Below is an example of absolute value being used as a decorator. Notice how the two functions ('add_no_dec' and 'add_dec') are the same (and have the same inputs). The only difference is the decorator is added before one of the function declarations.

    def abs_val(func): # name of function becomes name of decorator
        def wrapper(a,b):
            # takes the abs_val of the result of the function being wrapped
            return abs(func(a,b)) 
        return wrapper

    def add_no_dec(a,b):
        return a + b

    @abs_val    # the decorator always has an @ symbol followed by the name of the decorator function
    def add_dec(a,b):
        return a + b

    print('No Decorator')
    print(add_no_dec(-2,-3)) -> -5

    print('Decorator')
    print(add_dec(-2,-3)) -> 5

### Recursive Functions (example done)
A recursive function is one that calls itself as a part of the function. The famous example of this is to find the nth fibonnaci number. The function to do this only is defined to find the number before it. Within the function, there is another function call to find the number before it, and so on. The only acception to this is if the function is trying to determine the first or second fibonnaci numbers. In this case, both the first and second are equal to 1. The example below described the function I am talking about. The code example will be in the algorithms folder.

## Data Structures

## Input and Output

## Errors and Exceptions

### Try/Except (example done)
Often times when bulding a real program, on a webpage or local application, the user will enter something wrong (i.e. a string instead of a number) or another error comes up. In these cases, using a 'try/except block' can help prevent the program from crashing. Below is the general process of how the code works. In the example, the user is asked to input a number (which python will convert to an int). If the user enters something which cannot be converted to an integer, an error will occur. Without eh try/except block, the program would crash causing an error. With this extra code, we can plan for the error and print something esle out to the user to inform them of the error.

    try:
        num = int(input('Enter a number: '))
        print(num)
    except:
        print('Invalid input.')

While this is a simple example, you can use the same code to create more complex error handling. Beyond this basic concept, you can also write exception to handle particular types of errors. For example, if you are writing a calculator program, a user might type numbers in correctly but try to divide by zero. In this case, there should be a separate error message for divinding by zero and a separate message for invalid input. 

In the example below a function is defined which will attempt to divide two numbers. In the code there are exceptions to make sure the user is inputing information correct. Since two numbers are required, if there is an error in the input, the function will just return 'Error' after printing the error message. After there are no errors for the inputs, the function will try to run the divide function with the exception if a divide by zero error comes up during the division.

    def divide():
        print('Please enter two integers.')
        try:
            a = int(input('a = '))
        except ValueError as a_err:
            print(f'Error = {a_err}')
            return 'Error'                  # Only returning 'Error' because otherwise the output would be 'None'
    
        try:
            b = int(input('b = '))
        except ValueError as b_err:
            print(f'Error = {b_err}')
            return 'Error'


        return a/b                          # There is no exception for ZeroDivisionError here because no actual division takes place until the function is run

    try:
        answer = divide()
        print(answer)
    except ZeroDivisionError as zero_err:    # Exception for ZeroDivisionError here
        print(f'Error = {zero_err}')

It is considered a best practice in Python to make sure ALL except statements have an error after them. Without this, catching ANY error would run the same code. This could actually cause more errors in the code. See below for the list of all errors (and more will be added as needed).

### List of Errors for Except Statement

1. ValueError: Descrition here
2. ZeroDivisionError

## Classes

### What is a class?

### Inheritence
Inheritance is the ability to take properties and methods from a parent class down to a child class. In the example below, we will have two classes: the person class (the parent class in this case) and the teacher class (the child class in this case). The person class will have two properties and a method. The two properties are first name and last name and the method is say_hi which just prints hi. These methods (from the person class) are passed down to the teacher class. The teacher class specifically has one additional property (subject) and two additional methods: teach and grade. The teach method will just print "I am teaching" and the grade method will just print "[first_name] am grading".

    # this is an example of inheritance for classes in python

    # parent class
    class Person:

        def __init__(self,first_name,last_name):
            self.first_name = first_name
            self.last_name = last_name

        def say_hi(self):
            print("Hi!")

    # child class which inherits the properties of the person class
    class Teacher(Person):

        def __init__(self, first_name, last_name, subject):
            super().__init__(first_name, last_name) # This is what passes the class properties and methods down
            self.subject = subject

        def teach(self):
            print(f"I am teaching {self.subject}.")

        def grade(self):
            print(f'{self.first_name} is grading.')

    brian = Teacher("Brian","Murray","Math")
    
### Next classes topic

print(brian.say_hi())
print(brian.grade())

## Scope

### Global Scope

### Local Scope

By default, each variable created only has local scope. This, for example, means that if a variable is created in a function, it is only accessible from the function. There are ways to change this should the variable be needed outside the scope of the function. 

### Nonlocal Scope (example done)

"Nonlocal" is a keyword you can type before a variable name to change the scope of the variable. Consider the following example of a function which returns another function.

    def exp(n):
        def num(x):
            return x**n
        return num

    # this is the num function with a new name and n = 2
    squared = exp(2)

    squared(4) -> 16

In the example above, n could only be altered when a new 'num' function was created by passing the value of n into the 'exp' function. With the 'nonlocal' keyword, it is possible now to pull the n into the num function. In the example below, we will define n to be equal to 2 and then pull the variable into the num function.

In creating the square function, I will attempt to pass a different value of n (n=3). By doing this, it will be clear that the function 'num' is pulling the n variable from outside of its scope and setting n=2. 

    def exp(n):
        n=2   # outside local scope of 'num' function
        def num(x):
            nonlocal n  # special keyword that grabs n
            return x**n
        return num

    # attemping to make a cubed function x^3
    cubed = exp(3)

    cubed(4) -> 16   # not equal to 64 as intended
    
# Python Libraries

## Standard Library
These are the notes on the python standard library.

### Random package

## Pandas
Please note that when using Pandas, it is a common practice to use an alias instead of the whole "Pandas" word. See the code below for the pandas import statement.
    
    import pandas as pd
    
### How to read CSV files using Pandas

## NumPy

# Algorithms

## Fibonacci Number (example done)
The fibonacci number algorithm is a classic example of using recursive functions. In the function to find the nth fibonacci number, the function will call itself to find previous numbers in the sequence. The sequence is the following 1,1,2,3,5,8,13,21,... The example below gives (not the fastest) the most common approach to find the nth fibonacci number.

    # function to find the nth fibonacci number

    def fib_num(n):
        # returns 1 if the function is looking for the first two numbers
        if n == 1 or n == 2:
            return 1
        # the function will return the sum of the two numbers before it in the sequence
        else:
            return fib_num(n-2) + fib_num(n-1)

    print(fib_num(8)) # Result = 21
    
## Next Algorithm

# Testing

## What is testing and why is it important?

## Unit Testing

## PyTest

