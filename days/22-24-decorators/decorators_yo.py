"""
decorators -- add behaviour to a function -- behaviour can be added before and after the function
"""
from functools import wraps
import time

def mydecorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # do something before the original function is called
        # call the passed in function
        result = function(*args, **kwargs)
        # do something after the original function
        return result
    # return wrapper = decorated function
    return wrapper

@mydecorator
def my_function(args):
    pass

# non-common way of using a decorator -->
# def my_function(args):
#     pass
# my_function = mydecorator(my_function)