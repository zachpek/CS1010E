def freq_count(seq):
    result = {}
    for elem in seq:
        if elem not in result:
            result[elem] = 1
        else:
            result[elem] += 1
    return result
