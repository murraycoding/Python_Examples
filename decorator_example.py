def abs_val(func):
    def wrapper(a,b):
        return abs(func(a,b))
    return wrapper

def add_no_dec(a,b):
    return a + b

@abs_val
def add_dec(a,b):
    return a + b

print('No Decorator')
print(add_no_dec(-2,-3))

print('Decorator')
print(add_dec(-2,-3))