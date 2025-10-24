def koks_first_deep_count(lst):
    # this is shallow count
    if not lst:
        return 0
    return 1 + koks_first_deep_count(lst[1:])

def my_shot_deep_kok(lst):
    # kok said nested got similarities with recursion, so I can use recursion to manipulate/process nested sequences
    # illustrated well below when this solution was generalised to deep squares
    print(lst)
    if not lst:
        return 0
    current_elem = lst.pop()
    if type(current_elem) == list:
        return my_shot_deep_kok(lst + current_elem)
    return 1 + my_shot_deep_kok(lst)

def deep_count(lst):
    count = 0
    while lst:
        print(lst)
        first_elem = lst.pop()
        if type(first_elem) == list:
            lst.extend(first_elem)
        else:
            count += 1
    return count

def deep_square(seq):
    if not seq:
        return []
    first_element = seq[0]
    if type(first_element) == list:
        return [deep_square(first_element)] + deep_square(seq[1:])
    return [first_element ** 2] + deep_square(seq[1:])

def deep_square2(seq):
    result = []
    while seq:
        first_elem = seq.pop(0)
        if isinstance(first_elem, list):
            result.append(deep_square(first_elem))
        else:
            result.append(first_elem ** 2)
    return result

def deep_increment_tup(seq):
    # doesnt work idk why
    # In [5]: deep_increment_tup((1,2,3,(4,5),(6,(7))))
    # Out[5]: (2, 3, 4, (5, 6), (7, 8))
    if not seq:
        return ()
    first_element = seq[0]
    if type(first_element) == tuple:
        return (deep_increment_tup(first_element),) + deep_increment_tup(seq[1:])
    return (first_element + 1,) + deep_increment_tup(seq[1:])

def deep_map(fn, lst):
    # generalise the above (deep_square and deep_increment)
    if not lst:
        return []
    first_elem = lst[0]
    if type(first_elem) == list:
        return [deep_map(fn, first_elem)] + deep_map(fn, lst[1:])
    return [fn(first_elem)] + deep_map(fn, lst[1:])

# but the thing above keeps on slicing and creating lists - very inefficient
def deep_map2(fn, lst):
    result = []
    for elem in lst:
        if isinstance(elem, list):
            result.append(deep_map2(fn, elem))
        else:
            result.append(fn(elem))
    return result

def flatten(lst):
    if not lst:
        return []
    elem = lst[0]
    if type(elem) == list:
        return flatten(elem) + flatten(lst[1:])
    else:
        return [elem] + flatten(lst[1:])
    
def flatten2(lst):
    if not lst:
        return []
    if type(lst[0]) != list:
        result = [lst[0]]
    else:
        result = flatten2(lst[0])
    result.extend(flatten2(lst[1:]))
    return result

def flatten3(lst):
    result = []
    for elem in lst:
        if type(elem) != list:
            result.append(elem) # append if it's not a list
        else:
            result.extend(flatten3(elem)) # extend if it's a list
    return result
