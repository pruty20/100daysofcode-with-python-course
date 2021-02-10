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

"""
About args and kwargs functions
"""
# def get_profile(name, active=True, *sports, **awards):
#     print('Positional arguments (required): ', name)
#     print('Keyword arguments (not required, default values): ', active)
#     print('Arbitrary argument list (sports): ', sports)
#     print('Arbitrary keyword argument dictionary (awards): ', awards)

# print(get_profile())  # will return an error since 'name' is a positional argument
# print(get_profile('Razvan'))
# print(get_profile('Razvan', active=False))
# print(get_profile('Razvan', active=False, 'basketball', 'soccer'))  # will return an error since the system thinks a dictionary is being passed but it can be used as # print(get_profile('Razvan', False, 'basketball', 'soccer'))
# print(get_profile('Razvan', False, 'basketball', 'soccer',
#                   pythonista='special honor of the community', topcoder='2017 code camp'))


"""
using decorators
"""
def show_args(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print('hi from decorator - args:')
        print(args)
        result = function(*args, **kwargs)
        print('hi again from decorator - kwargs:')
        print(kwargs)
        return result
    # return wrapper as a decorated function
    return wrapper

@show_args
def get_profile(name, active=True, *sports, **awards):
    print('\n\thi from get_profile function\n')

get_profile('bob', True, 'basketball', 'soccer',
            pythonista='special honor of the community', topcoder='2017 code camp')


