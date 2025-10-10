# part 1

def list_filter_ite(func, lst):
    result = []
    for elem in lst:
        if func(elem):
            result.append(elem)
    return result

def lf_ls_compre(func, lst):
    return [elem for elem in lst if func(elem)]

def list_filter_rec(func, lst):
    # oh dear, slicing the list after elif creates a new list - the creation of said list wastes space
    # and list slicing doesn't exist in other languages
    # so we use indexing instead of slicing as seen below in lf_khoo
    if not lst:
        return []
    elif func(lst[0]):
        return [lst[0]] + list_filter_rec(func, lst[1:]) # almost forgot to put lst[0] into a list
    else:
        return list_filter_rec(func, lst[1:])

def lf_khoo(func, lst):
    def helper(idx):
        if idx == len(lst):
            return []
        elif func(lst[idx]):
            return [lst[idx]] + helper(idx + 1)
        else:
            return helper(idx + 1)
    return helper(0)

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
