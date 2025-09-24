def matchResistors(R, n):
    # Finds all pairs of resistors that can produce a total sum of n ohms.
    # 
    # Args:
    #     R (Union[tuple[Union[float, int], ...], list[Union[float, int], ...]]): Tuple or list of resistors given.
    #     n (float or int): Resistance value wanted.
    # 
    # Returns:
    #     tuple[tuple[int, int], ...]: Tuples of pairs of resistors that sum to n ohms.

    # sorted_list = sorted(R) # see if i fail any private cases
    half = n / 2
    i = 0
    j = -1
    next_j = -1
    matched = ()
    while R[i] <= half:
        while R[j] > half:
            if R[i] + R[j] == n:
                matched += ((R[i], R[j]),)
                next_j = j - 1
                break
            j -= 1
        j = next_j
        i += 1
    return matched