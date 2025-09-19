# henry's practices

def maxi(tup):
    if len(tup) == 1:
        return tup[0]
    a = maxi(tup[:-1])
    if a > tup[-1]:
        return a
    else:
        return tup[-1]
    
def maxi_henry(tup):
    if len(tup) == 1:
        return tup[0]
    a = maxi_henry(tup[1:])
    if a > tup[0]:
        return a
    else:
        return tup[0]
    
def adj_pair(tup):
    if len(tup) == 2:
        return tup, tup[0] + tup[1]
    pair, next_s = adj_pair(tup[1:])
    current_s = tup[0] + tup[1]
    if next_s > current_s:
        return pair, next_s
    else:
        # no need indicate "else": just return on the next lin
        # gives u a long ahh tuple: return (tup, current_s)
        return tup[:2], current_s
    
def adj_pair_henry(tup):
    if len(tup) == 2:
        return (tup, sum(tup))
    a, b = adj_pair_henry(tup[1:])
    here = tup[0] + tup[1]
    if here > b:
        return(tup[0:2], here)
    return (a, b)

# part 1 recursion

def burgerPriceW5(burger):
    def ingredient_price(ingredient):
        return 0.5 if ingredient == 'B' \
            else 0.8 if ingredient == 'C' \
            else 1.5 if ingredient == 'P' \
            else 0.7 if ingredient == 'V' \
            else 0.4 if ingredient == 'O' \
            else 0.9 if ingredient == 'M' \
            else None
    return sum(map(ingredient_price, burger))


def ingredient_price(ingredient):
    return 0.5 if ingredient == 'B' \
        else 0.8 if ingredient == 'C' \
        else 1.5 if ingredient == 'P' \
        else 0.7 if ingredient == 'V' \
        else 0.4 if ingredient == 'O' \
        else 0.9 if ingredient == 'M' \
        else None
    
def burgerPrice(burger):
    return ingredient_price(burger[0]) + burgerPrice(burger[1:]) if len(burger) > 1 else ingredient_price(burger)

def burgerPriceAnother(burger):
    return ingredient_price(burger[-1]) + burgerPrice(burger[:-1]) if burger else 0

def burger_price_henry(burger):
    if burger == '':
        return 0
    return ingredient_price(burger[0]) + burger_price_henry(burger[1:])

def ne(x, y):
    if x == 0 or y == 0:
        return 1
    return ne(x - 1, y) + ne(x, y - 1)

# part 2 recursion vs iteration

def digit_sum_rec(n):
    return digit_sum_rec(n // 10) + n % 10 if n // 10 else n

def digit_sum_rec_2(n):
    return n % 10 + digit_sum_rec(n // 10) if n else 0

def digit_sum_ite(n):
    summed = 0
    while n:
        summed += n % 10
        n = n // 10
    return summed

def final_digit_sum_rec(n):
    intermediate = final_digit_sum_rec(n // 10) + n % 10 if n else 0
    if intermediate // 10:
        return final_digit_sum_rec(intermediate)
    return intermediate

def final_digit_sum_ite(n):
    summed = n
    while summed // 10:
        summed = 0
        while n:
            summed += n % 10
            n = n // 10
        n = summed
    return summed

from math import factorial

def find_e_rec(x, n):
    return x ** n / factorial(n) + find_e_rec(x, n - 1) if n else 1

def find_e_ite(x, n):
    summed = 1
    while n:
        summed += x ** n / factorial(n)
        n -= 1
    return summed

def find_e_ite_for(x, n):
    summed = 1
    for i in range(1, n+1):
        summed += x ** i / factorial(i)
    return summed