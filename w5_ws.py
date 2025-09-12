# part 2

def print_stars_long(n):
    '''demonstrates the use of an ACCUMULATOR
    "that's what you always use" ~ khoo'''
    for rows in range(n, 0, -1):
        # first, initialise my accumulator
        toprint = '' # called the accumulator - variable to accumulate the answer you want
        for j in range(rows):
            toprint += '*'
        print(toprint)

def print_stars_less_long(n):
    for rows in range(n, 0, -1):
        for _ in range(rows):
            print('*', end = '')
        print('')

def print_stars(n):
    for i in range(n, 0, -1):
        print('*' * i)

def print_hashes(n):
    for i in range(n):
        print('#' + ' ' * i + '#')

# part 3

from math import *

def taylor_cos(x, d):
    n = 0
    series = 0
    nth_taylor_cos = lambda n: (-1) ** n / factorial(2 * n) * x ** (2 * n)
    term = nth_taylor_cos(n)
    series += term
    n += 1
    while abs(term) >= d:
        term = nth_taylor_cos(n)
        series += term
        n += 1
    return series

# part 4

def burgerPriceDumb(burger):
    price = 0
    buns = sum(filter(lambda letter: letter == 'B', burger)) * 0.5
    return price

def burgerPrice(burger):
    def ingredient_price(ingredient):
        return 0.5 if ingredient == 'B' else 
    return sum(map(ingredient_price, burger))

# part 5:
