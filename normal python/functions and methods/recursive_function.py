# Recursive Function 

def recursive_function(a,b):
    print(f'Function is called with a={a} and b={b}')
    while a < b:
        recursive_function(a+1,b-1)
        return

recursive_function(1,10)
