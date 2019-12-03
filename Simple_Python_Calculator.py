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

dict_operations = {'options':{'add':' perform the addition of two integers',
                              'sub':' perform the subtraction of two integers', 
                              'multi':' perform the multiplication of two integers', 
                              'divide':' perform the division of two numbers', 
                              'exp':' get the result of a base integer with exponential factor of another integer', 
                              'root':' get the nth integer root of a base integer'}}
dict_functions = {
    'add': add,
    'sub': sub,
    'multi': multi,
    'divide': divide,
    'exp' : exp,
    'root' : root,
}

active = True #Flag set for program runtime

print("Welcome to the Simple Python Calculator. Please enter an operation to perform.")

while active:
    sel = input("\nEnter operation on this line or enter help to see options or quit: ")

    if sel == 'help':
        for key, vals in dict_operations.items():
            print("Here are your choices of "+ key +":")
            for each, description in vals.items():
                print("\n" + each + ':' + description + '.')

    elif sel == 'quit':
        active = False 

    else:
        for each in dict_functions.keys():
            if sel == each :
                arg1 = int(input("\nEnter the first integer argument of your operation: "))
                arg2 = int(input("\nEnter the second integer argument of your operation: "))
                for defs in dict_operations['options']:
                    if sel == defs:
                        print("\nThe result is: " + str(dict_functions[sel](arg1,arg2)))
            else:
                continue          

print("\nThank you for using the Simple Python Calculator.")