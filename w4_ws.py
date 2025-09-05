from math import factorial
from functools import reduce

def sds(n):
    return sum(map(lambda x: int(x) ** 2, str(n))) # hmm prof khoo enclosed the map output within tuple()

def taylor_sin_20(x):
    return sum(map(lambda n: (-1) ** n / factorial(2 * n + 1) * x ** (2 * n + 1), range(20))) # prof khoo said he thinks range(7 or 8 or 9) would be good

def taylor_cos_20(x):
    return sum(map(lambda n: (-1) ** n / factorial(2 * n) * x ** (2 * n), range(20)))

def taylor_cos(x, k):
    # prof's ans
    term = lambda n: (x**(2*n) * ((-1)**n)) / factorial(2*n)
    return sum(map(term, range(k + 1)))

def get_cos(k):
    # even better
    def tcos(x):
        term = lambda n: (x**(2*n) * ((-1)**n)) / factorial(2*n)
        return sum(map(term, range(k + 1)))
    return tcos        

def d_elem_red_n_map(t):
    return tuple(reduce(lambda y, z: y + z, map(lambda x: (x, x), t)))

def d_elem_red_only(t):
    return tuple(reduce(lambda x, y: x + (y, y), t, ()))

# stuff in class:
test = lambda a: lambda b: lambda c: a + b + c

# In [1]: from w4_ws import test

# In [2]: test(1)
# Out[2]: <function w4_ws.<lambda>.<locals>.<lambda>(b)>

# In [3]: test(1)(2)
# Out[3]: <function w4_ws.<lambda>.<locals>.<lambda>.<locals>.<lambda>(c)>

# In [4]: test(1)(2)(3)
# Out[4]: 6