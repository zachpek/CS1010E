# recursive

def s(seq):
    return seq[-1] + s(seq[:-1]) if seq else 0

def cumsum(seq):
    # ok actl maybe this isnt so recursive after all??
    return cumsum(seq[:-1]) + (s(seq),) if seq else ()

def cumsum_henry(seq):
    if len(seq) <= 1:
        return seq # neat, one less cycle than mine
    lst = cumsum_henry(seq[:-1])
    return lst + (lst[-1] + seq[-1],) # nice, cumsum logic here already