def up_adj_strR(tup):
    less = tup[0] < tup[1]
    if len(tup) == 2:
        return ((tup[0], tup[1]),) if less \
            else ()
    next_tup = up_adj_strR(tup[1:])
    if less:
        return (tup[:2],) + next_tup
    return next_tup
