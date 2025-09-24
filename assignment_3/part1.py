def matchResistors(R, n):
    # Finds all pairs of resistors that can produce a total sum of n ohms.
    # 
    # Args:
    #     R (Union[tuple[Union[float, int], ...], list[Union[float, int], ...]]): Tuple or list of resistors given.
    #     n (float or int): Resistance value wanted.
    # 
    # Returns:
    #     tuple[tuple[Union[float, int], Union[float, int]], ...]: Tuples of pairs of resistors that sum to n ohms.

    sorted_list = sorted(R)
    half = n / 2
    i = 0
    j = -1
    next_j = -1
    matched = ()
    while sorted_list[i] <= half:
        while sorted_list[j] > half:
            if sorted_list[i] + sorted_list[j] == n:
                matched += ((sorted_list[i], sorted_list[j]),)
                next_j = j - 1
                break
            j -= 1
        j = next_j
        i += 1
    return matched