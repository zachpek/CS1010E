def num_of_ways(n):
    # Calculates the number of ways Fabulous can take n number of meals such that no 2 consecutive meals are fast food meals.
    # 
    # Args:
    #     n (int): The total number of meals.
    # 
    # Returns:
    #     int: The number of possible ways.

    if n == 1:
        return 2
    elif n == 2:
        return 3
    return num_of_ways(n - 1) + num_of_ways(n - 2)