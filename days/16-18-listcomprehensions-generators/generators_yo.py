import calendar, timeit

def num_gen():
    for i in range(5):
        yield i

gen = num_gen()

# # printing the next value from the generator
# print(next(gen))
#
# # it started to print from 1 since 0 was already returned from the previous statement
# for i in gen:
#     print(i)

# # having another "next" try on a generator that was already exhausted will throw an exception
# # but will not throw an exception in the case that a for loop is being used
# # even if the generator would seem to be exhausted at the end
# print(next(gen))

options = "red yellow blue white black green purple".split()

# # using an old approach
# def create_select_options(options=options):
#     select_list = []
#     for option in options:
#         select_list.append(f"<option value={option}>{option.title()}</option>>")
#
#     return select_list
#
# from pprint import pprint as pp
# pp(create_select_options())

# using generators
def create_select_options_gen(options=options):
    for option in options:
        yield f"<option value={option}>{option.title()}</option>>"

# # convert the generator into a list
# select_options_list = list(create_select_options_gen())

# Comparing lists vs generators
# list
def leap_years_lst(n=100):
    leap_years = []
    for year in range(1, n+1):
        if calendar.isleap(year):
            leap_years.append(year)

    return leap_years

# generator
def leap_years_gen(n=100000):
    for year in range(1, n+1):
        if calendar.isleap(year):
            yield year


# # you can run it with python3 and the absolut path
if __name__ == '__main__':
    import timeit
    # print(timeit.timeit("leap_years_gen()", setup="from __main__ import leap_years_gen"))
    print(timeit.timeit("leap_years_lst()", setup="from __main__ import leap_years_lst"))


