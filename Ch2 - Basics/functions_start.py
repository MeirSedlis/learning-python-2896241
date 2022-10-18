#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def func1():
    print("I am a function")

# TODO: function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# TODO: function that returns a value
def cube(x):
    return x * x * x

# TODO: function with default value for an argument
def power(num, x=1):
        result = 1;
        for i in range(x):
            result = result * num
        return result

# TODO: function with variable number of arguments
  # this is basically an accumulator function like reduce
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


# func1() # calling the function directly prints the string
# print(func1()) # the function is still being called inside the print statement so the string still prints
# print(func1) # there is no return value so this prints None and then a function object which is meaningless in terminal but interesting nonetheless

# func2(10, 20) # will print these numbers separated by a space
# print(func2(10, 20)) # will print the same thing as above + None because there is no return value
# print(cube(3)) # will print 27

# print(power(2)) # calling the function with no value for x meaning this should return 2^1 or 2
# print(power(2, 3)) # calls the function with x=3 meaning this should return 2^3  or 8
# print(power(x=3, num=2)) # python lets you change the order of the arguments if you supply the names along with the values. this should still return 8.

print(multi_add(4,5,10,4,10))