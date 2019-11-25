# ---- Simple Python Calculator ---- #
# Please use the README for instructions on how to use this program #

def add(x,y):
    """Return the addition of two integer arguments."""
    return x+y

def sub(x,y):
    """Return the subtraction of two integer arguments."""
    return x-y

def multi(x,y):
    """Return the multiplication of two integer arguments."""
    return x*y

def divide(x,y):
    """Return the division of two integer arguments."""
    return (x/y)

def exp(x,y):
    """Return the exponential of two integer arguments.
    The first argument is the base number.
    The second argument is the exponential factor.
    """
    return x**y

def root(x, y):
    """Return the n root of an integer argument by a factor of a second integer argument."""
    return x**(1/float(y))

dict_operations = {'options':['add', 'sub', 'multi', 'divide', 'exp', 'root']}
dict_functions = {
    'add': add,
    'sub': sub,
    'multi': multi,
    'divide': divide,
    'exp' : exp,
    'root' : root,
}

print("Welcome to the Simple Python Calculator. Please enter an operation to perform.")

while True:
    sel = input("\nEnter operation on this line or enter help to see options or quit: ")

    if sel == 'help':
        for key, vals in dict_operations.items():
            print("Here are your choices of "+ key +":")
            for each in vals:
                print("\n" + each)

    elif sel == 'quit':
        break
    
    else:
        arg1 = int(input("\nEnter the first integer argument of your operation: "))
        arg2 = int(input("\nEnter the second integer argument of your operation: "))
        for defs in dict_operations['options']:
            if sel == defs:
                print("\nThe result is: " + str(dict_functions[sel](arg1,arg2)))


print("\nThank you for using the Simple Python Calculator.")