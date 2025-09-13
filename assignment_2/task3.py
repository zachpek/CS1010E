def sum1(seq):
    # Takes in a tuple of integers and prints out each value on a separate line.
    # In addition, alongside each 𝑖 th value, output the cumulative sum (i.e. the sum of all values from the first value up till and including the 𝑖 th one).
    # 
    # Args:
    #     seq (tuple[int, ...]): Tuple of integers to print and calculate the cumulative sum of.
    # 
    # Returns:
    #     None: This function only prints values.
    
    cumulative_sum = 0
    for i in range(len(seq)):
        ith_value = seq[i]
        cumulative_sum += ith_value
        print('{},{}#'.format(ith_value, cumulative_sum))

def sum2(seq):
    # Takes in a tuple of integers and prints out each value on a separate line.
    # In addition, alongside each 𝑖 th value, output the cumulative sum (i.e. the sum of all values from the first value up till and including the 𝑖 th one).
    # Finally, after all values and cumulative sums have been printed, prints the maximum of all cumulative sums.
    #
    # Args:
    #     seq (tuple[int, ...]): Non-empty tuple of integers to print and calculate the cumulative sum of.
    # 
    # Returns:
    #     None: This function only prints values.
    
    cumulative_sum = 0
    max_cumulative_sum = seq[0] # Takes the first element of the tuple argument as the cumulative sum will be greater than or equal to the first element of the tuple. Assumes that the tuple is not empty.
    for i in range(len(seq)):
        ith_value = seq[i]
        cumulative_sum += ith_value
        print('{},{}#'.format(ith_value, cumulative_sum))

        if cumulative_sum > max_cumulative_sum:
            max_cumulative_sum = cumulative_sum
    print('{}#'.format(max_cumulative_sum))

def sum3(seq):
    # Takes in a tuple of integers and prints out each value on a separate line.
    # In addition, alongside each 𝑖 th value, output the cumulative sum of the current subsequence. If the current cumulative sum is negative, the cumulative sum will be restarted/reset to 0 - the subsequence considered for the cumulative sum will start from the next element.
    # Finally, after all values and cumulative sums have been printed, prints the maximum over all cumulative sums with restart, which is also the maximum sum of sub-sequences.
    #
    # Args:
    #     seq (tuple[int, ...]): Non-empty tuple of integers to print and calculate the cumulative sum of.
    # 
    # Returns:
    #     None: This function only prints values.
    
    cumulative_sum = 0
    max_cumulative_sum = seq[0] # Takes the first element of the tuple argument as the cumulative sum will be greater than or equal to the first element of the tuple. Assumes that the tuple is not empty.
    for i in range(len(seq)):
        ith_value = seq[i]
        if cumulative_sum < 0:
            cumulative_sum  = 0
        cumulative_sum += ith_value
        print('{},{}#'.format(ith_value, cumulative_sum))

        if cumulative_sum > max_cumulative_sum:
            max_cumulative_sum = cumulative_sum
    print('{}#'.format(max_cumulative_sum))

def sum4(lst):
    # Takes in a tuple of integers and prints out each value on a separate line.
    # In addition, alongside each 𝑖 th value, output the cumulative sum of the current subsequence. If the current cumulative sum is negative, the cumulative sum will be restarted/reset to 0 - the subsequence considered for the cumulative sum will start from the next element.
    # Finally, after all values and cumulative sums have been printed, prints the maximum over all cumulative sums with restart, which is also the maximum sum of sub-sequences. Print also the index/indices of the start/end of this sub sequence.
    #
    # Args:
    #     lst (tuple[int, ...]): Non-empty tuple of integers to print and calculate the cumulative sum of.
    # 
    # Returns:
    #     None: This function only prints values.
    
    cumulative_sum = 0
    max_cumulative_sum = lst[0] # Takes the first element of the tuple argument as the cumulative sum will be greater than or equal to the first element of the tuple. Assumes that the tuple is not empty.
    subsequence_start_position = 1
    subsequence_end_position = 1
    potential_subsequence_start_index = 0
    potential_subsequence_end_index = 0
    for i in range(len(lst)):
        ith_value = lst[i]
        if cumulative_sum <= 0:
            cumulative_sum  = 0
            potential_subsequence_start_index = i
        cumulative_sum += ith_value
        print('{},{}#'.format(ith_value, cumulative_sum))

        if cumulative_sum > max_cumulative_sum:
            max_cumulative_sum = cumulative_sum
            potential_subsequence_end_index = i
            subsequence_start_position, subsequence_end_position = potential_subsequence_start_index + 1, potential_subsequence_end_index + 1
    print('{}({},{})#'.format(max_cumulative_sum,subsequence_start_position,subsequence_end_position))