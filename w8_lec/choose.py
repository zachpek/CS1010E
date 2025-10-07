def choose(n, k):
    if k > n:
        return 0
    elif k == 0 or n == k:
        return 1
    else:
        return choose(n - 1, k) + choose(n - 1, k - 1)

def memo_choose(n_wanted, k_wanted):
    results = {}
    def choose(n, k):
        if k > n:
            return 0
        nk_combi = (n, k)
        if nk_combi in results:
            return results[nk_combi]
        elif k == 0 or n == k:
            return 1
        else:
            nck = choose(n - 1, k) + choose(n - 1, k - 1)
            results[nk_combi] = nck
            return nck
    return choose(n_wanted, k_wanted)
