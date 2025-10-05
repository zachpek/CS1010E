# part 1

def list_filter_ite(func, lst):
    result = []
    for elem in lst:
        if func(elem):
            result.append(elem)
    return result

def list_filter_rec(func, lst):
    if not lst:
        return []
    elif func(lst[0]):
        return [lst[0]] + list_filter_rec(func, lst[1:]) # almost forgot to put lst[0] into a list
    else:
        return list_filter_rec(func, lst[1:])

# part 2

def deep_filter_rec(func, lst):
    if not lst:
        return []
    elif isinstance(lst[0], list):
        return [deep_filter_rec(func, lst[0])] + deep_filter_rec(func, lst[1:])
    else:
        if func(lst[0]):
            return [lst[0]] + deep_filter_rec(func, lst[1:])
        else:
            return deep_filter_rec(func, lst[1:])

def deep_filter_hybrid(func, lst):
    result = []

    for elem in lst:
        if isinstance(elem, list):
            result.append(deep_filter_hybrid(func, elem))
        else:
            if func(elem):
                result.append(elem)

    return result
