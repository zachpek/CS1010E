def invert_dict(dic):
    result = {}
    for k, v in dic.items():
        if v not in result:
            result[v] = [k]
        else:
            result[v].append(k) # result[v] += [k]
    return result
