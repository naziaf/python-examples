def sayHello(name):
    return "Hello " + name + "!"

def sayHelloAgain(name='Roshith'):
    return f"Hello {name}!"

# print(dir(sayHello("Pratik")))
print(sayHello("Pratik"))
print(sayHelloAgain("Pratik"))
# When a function without a value for an argument, its default value is used.
print(sayHelloAgain())    # Roshith

print("__________________Passing Multiple Arguments to a Function____________________")
def multiply(a, b):
    print("{0} * {1} = {2}".format(a, b, a*b))

multiply(2, 4)
multiply(a=2, b=4)
multiply(b=4, a=2)

# Positional Arguments : (*args)
# You would use *args when you're not sure how many arguments might be passed to your function,
# i.e. it allows you pass an arbitrary number of arguments to your function."""

def positional_args_sum(*integers):     # unpacking operator (*)
    print("\nInput (*args) python args tuple:", integers)
    result = 0
    for x in integers:
        result += x
    return result

print("positional_args_sum(1, 2, 3) :", positional_args_sum(1, 2, 3))
print("positional_args_sum() :", positional_args_sum())

# Keyword (or named) arguments.  **kwargs
# **kwargs allows you to handle named arguments that you have not defined in advance
def named_agrs_func(**input_pars):
    # Iterating over the Python kwargs dictionary
    print("\nInput (*kwargs) python kwargs dict:", input_pars)
    for k, v in input_pars.items():
        print(k, '->', v)

# Function call
named_agrs_func(par1="hello", par2=True, par3=[1, 2, 3])

