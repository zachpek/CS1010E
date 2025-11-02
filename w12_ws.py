def bubble(lst):
    bubbled = lst.copy()
    for i in range(1, len(bubbled)):
        if bubbled[i - 1] > bubbled[i]:
            bubbled[i - 1], bubbled[i] = bubbled[i], bubbled[i - 1]
    return bubbled

def bubble_sort(lst):
    sort_alr = lst
    for _ in range(len(sort_alr)):
        sort_alr = bubble(sort_alr)
    return sort_alr

def bisection(f, a, b, epsilon):
    # a < b, such that f(a) > 0 and f(b) < 0
    #  if both f(a) and f(b) have the same sign, we should not proceed with the search because there may be no solution in the interval, and this will cause the bisection method to get into an infinite loop
    if f(a) * f(b) > 0:
        return None
    if f(a) < f(b):
        a, b = b, a
    xm = (a + b) / 2
    fxm = f(xm)
    if fxm < 0:
        return bisection(f, a, xm, epsilon)
    if fxm < epsilon:
        return xm
    return bisection(f, xm, b, epsilon)
