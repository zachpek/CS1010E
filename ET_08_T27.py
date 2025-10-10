# Name: Pek Tze Hng, Zachary
# NUSNET ID: E1525681
# Question Number: 4

def p4R(lst):
    # given a (posssibly empty and possibly nested) list lst containing integers,
    # produces a new list in which all integers from lst have been converted to string data type.
    # constraints:
    #     - use recursion
    #     - no loop construct allowed
    # 
    # after this submission, try to develop a similar function p4L(lst) which produces the result using .append() method.

    if not lst:
        return []
    elem = lst[0]
    if type(elem) == list:
        result = [p4R(elem)]
    else:
        result = [str(elem)]
    result.extend(p4R(lst[1:]))
    # got stuck here: tried to return the above line and hence the function treid to extend result with a NoneType.
    # append, extend, remove (and more) list methods return None.
    return result

def p4L(lst):
    result = []
    for elem in lst:
        if type(elem) == list:
            result.append(p4L(elem))
        else:
            result.append(str(elem))
    return result
