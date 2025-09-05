import math
from functools import reduce

def maclaurin_asinh(x, k):
    term = lambda k: (((-1) ** k * math.factorial (2 * k)) / (4 ** k * math.factorial(k) ** 2 * (2 * k + 1))) * x ** (2 * k + 1)
    return sum(map (term, range(1 + k)))
