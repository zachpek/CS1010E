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
    left, right = 0, len(sorted_list) - 1
    matched = ()
    while left < right:
        current_sum = sorted_list[left] + sorted_list[right]
        if current_sum == n:
            matched += ((sorted_list[left], sorted_list[right]),)
            left += 1
            right -= 1
        elif current_sum < n:
            left += 1
        else:
            right -= 1
    return matched