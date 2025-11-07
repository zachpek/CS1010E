# Name: Pek Tze Hng, Zachary
# NUSNET ID: e1525681
# Question Number: 2

def sort2(L):
    # Define a Python function sort2(L) which performs in-place sorting to convert a partially sorted input list L into a fully sorted list (in non-descending order).
    # The input list has the characteristics that all of its elements, except the first element, are already sorted in non-descending order.
    # The first element may not have been sorted.

    n = len(L)
    i = 0
    while i < n - 1 and L[i] > L[i + 1]:
        L[i], L[i + 1] = L[i + 1], L[i]
        i += 1

    print(L)
