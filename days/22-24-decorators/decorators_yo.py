"""
decorators -- add behaviour to a function -- behaviour can be added before and after the function
"""
from functools import wraps
import time

# def mydecorator(function):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         # do something before the original function is called
#         # call the passed in function
#         result = function(*args, **kwargs)
#         # do something after the original function
#         return result
#     # return wrapper = decorated function
#     return wrapper
#
# @mydecorator
# def my_function(args):
#     pass

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
# def show_args(function):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         # doing something before the original function is called
#         print('hi from decorator - args:')
#         print(args)
#         result = function(*args, **kwargs)
#         # doing something after the original function
#         print('hi again from decorator - kwargs:')
#         print(kwargs)
#         return result
#     # return wrapper as a decorated function
#     return wrapper
#
# @show_args
# def get_profile(name, active=True, *sports, **awards):
#     print('\n\thi from get_profile function\n')
#
# get_profile('bob', True, 'basketball', 'soccer',
#             pythonista='special honor of the community', topcoder='2017 code camp')

"""
Writting a timeit decorator
"""
def timeit(func):
    """Decorator to time a function"""
    @wraps(func)
    def wrapper(*args, **kwargs):

        # before calling the decorated function
        print('== starting timer')
        start = time.time()

        # call the decorated function
        func(*args, **kwargs)

        # after calling the decorated function
        end = time.time()
        print(f'== {func.__name__} took {int(end-start)} seconds to complete')

    return wrapper()

# @timeit
# def generate_report():
#     """Function to generate revenue report"""
#     time.sleep(2)
#     print('(actual function) Done, report links...')


##  for some reason the generate_report() is called by default without calling the actual function
# generate_report()

"""
stacking decorators --> bellow code will throw an exception -- need to investigate when time
"""
def print_args(func):
    """Decorator to print function arguments"""
    @wraps(func)
    def wrapper(*args, **kwargs):

        # before
        print()
        print('*** args:')
        for arg in args:
            print(f'- {arg}')

        print('**** kwargs:')
        for k, v in kwargs.items():
            print(f'- {k}: {v}')
        print()

        # call func
        func(*args, **kwargs)
    return wrapper

# @timeit
# @print_args
# def generate_report(*months, **parameters):
#     time.sleep(2)
#     print('(actual function) Done, report links...')

# parameters = dict(split_geos=True, include_suborgs=False, tax_rate=3)
#
#
# generate_report('October', 'November', 'December', **parameters)























