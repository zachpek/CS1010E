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
        # if ingredient == 'B':
        #     return 0.5
        # elif ingredient == 'C':
        #     return 0.8
        # elif ingredient == 'P':
        #     return 1.5
        # elif ingredient == 'V':
        #     return 0.7
        # elif ingredient == 'O':
        #     return 0.4
        # elif ingredient == 'M':
        #     return 0.9
        return 0.5 if ingredient == 'B' \
            else 0.8 if ingredient == 'C' \
            else 1.5 if ingredient == 'P' \
            else 0.7 if ingredient == 'V' \
            else 0.4 if ingredient == 'O' \
            else 0.9 if ingredient == 'M' \
            else None
    return sum(map(ingredient_price, burger))

# part 5:

from mealOrders import *

def enoughMoney(order, moneyInMyPocket):
    return moneyInMyPocket >= sum(map(burgerPrice, order))

def printReceipt(order):
    total_price = 0
    print('Your orders:')
    for burger in order:
        price = burgerPrice(burger)
        total_price += price
        print(f'{burger} ${price}')
    print('-' * 14)
    print(f'Total: {total_price}')

def removeOrder(order, item):
    if item in order:
        order_to_return = ()
        for borgar in order:
            if borgar != item:
                order_to_return += (borgar,) # oh no this removes multiple occurrences of the item in the order
        return order_to_return            
    else:
        print('not in order alr')

def removeOrderHenry(order, item):
    if not item in order:
        print(f'The item {item} is not in the order.')
        return order
    result = ()
    found = False
    for itm in order:
        if found or item != itm:
            result += (itm,)
        else:
            found = True # nice, so after the first occurence of itm every element will be appended to the tuple
    return result