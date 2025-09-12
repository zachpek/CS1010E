def down_adj_str_idx(tup):
    res = ()
    for i in range(len(tup) - 1):
        if tup[i] > tup[i + 1]:
            res += ((i, i+1),)
    return res