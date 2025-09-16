def cumsum(lst):
    return [lst[i] + lst[i-1] for i in range(1,len(lst))]

def cumsum_henry(lst):
    return [sum(lst[:i+1]) for i in range(len(lst))]