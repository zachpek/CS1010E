def cumsum(lst):
    # lol doesnt work
    # list lst is not being modified - a new list is being created in the list comprehension
    # and wrong number of elements (need same element as list)
    return [lst[i] + lst[i-1] for i in range(1,len(lst))]

def cumsum_henry(lst):
    return [sum(lst[:i+1]) for i in range(len(lst))]