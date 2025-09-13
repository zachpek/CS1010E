def sum1(lst):
    # Takes in a tuple of integers and prints out each value on a separate line.
    # In addition, alongside each 𝑖 th value, output the cumulative sum (i.e. the sum of all values from the first value up till and including the 𝑖 th one).
    # 
    # Args:
    #     lst (tuple[int, ...]): Tuple of integers to print and calculate the cumulative sum of.
    # 
    # Returns:
    #     None: This function only prints values.
    
    cumulative_sum = 0
    for i in range(len(lst)):
        ith_value = lst[i]
        cumulative_sum += ith_value
        print('{},{}#'.format(ith_value, cumulative_sum))

def sum2(lst):
    # Takes in a tuple of integers and prints out each value on a separate line.
    # In addition, alongside each 𝑖 th value, output the cumulative sum (i.e. the sum of all values from the first value up till and including the 𝑖 th one).
    # Finally, after all values and cumulative sums have been printed, prints the maximum of all cumulative sums.
    #
    # Args:
    #     lst (tuple[int, ...]): Tuple of integers to print and calculate the cumulative sum of.
    # 
    # Returns:
    #     None: This function only prints values.
    
    cumulative_sum = 0
    max_cumulative_sum = lst[0]
    for i in range(len(lst)):
        ith_value = lst[i]
        cumulative_sum += ith_value
        print('{},{}#'.format(ith_value, cumulative_sum))

        if cumulative_sum > max_cumulative_sum:
            max_cumulative_sum = cumulative_sum
    print('{}#'.format(max_cumulative_sum))