def divide():
    print('Please enter two integers.')
    try:
        a = int(input('a = '))
    except ValueError as a_err:
        print(f'Error = {a_err}')
        return 'Error'
    
    try:
        b = int(input('b = '))
    except ValueError as b_err:
        print(f'Error = {b_err}')
        return 'Error'


    return a/b

try:
    answer = divide()
    print(answer)
except ZeroDivisionError as zero_err:
    print(f'Error = {zero_err}')
