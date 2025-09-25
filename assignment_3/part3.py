def check(puzzle, mapping):
    # Checks if a given mapping is valid for the given puzzle.
    # 
    # Args:
    #     puzzle (tuple[str, ...]): Tuple of at least 2 elements, with the first (n - 1) elements being words to be added together, and the n-th element being the result that it should add up to.
    #     mapping (str): A string where each letter at index i is mapped to that integer i. A dot at index i means that there is no mapping from any letters to that integer i.
    # 
    # Returns:
    #     str or bool: Returns mapping if it is valid else returns False.
    
    # first, check if mapping given is valid
    puzzle_letters = ''
    for word in puzzle:
        puzzle_letters += word

    for letter in puzzle_letters:
        if letter not in mapping:
            return False

    mapping_letters = ''
    for letter in mapping:
        if letter != '.':
            if letter in mapping_letters or letter not in puzzle_letters:
                return False
            mapping_letters += letter
        
    # then, find the sum of the words
    summed_words = 0
    for i in range(len(puzzle)):
        number_word = ''

        for letter in puzzle[i]:
            number_word += str(letter_to_number(letter, mapping))

        # this checks for leading zeros after the digits for each word is computed
        if number_word[0] == '0':
            return False

        if i < len(puzzle) - 1:
            summed_words += int(number_word)
        else:
            final_sum = int(number_word)

    return mapping if summed_words == final_sum else False
    
def letter_to_number(letter, mapping):
    # Takes in a letter and returns its index based on a mapping.
    # 
    # Args:
    #     letter (str): A single letter to be checked against the mapping.
    #     mapping (str): A string where each letter at index i is mapped to that integer i. A dot at index i means that there is no mapping from any letters to that integer i.
    # 
    # Returns:
    #     int or None: Returns the index i the letter is mapped to if found.
    for i in range(len(mapping)):
        if letter == mapping[i]:
            return i
    return None

def unique_letters(puzzle):
    # Find out what alphabets are present within the puzzle.
    # 
    # Args:
    #     puzzle (tuple[str, ...]): Tuple of at least 2 elements, with the first (n - 1) elements being words to be added together, and the n-th element being the result that it should add up to.
    # 
    # Returns:
    #     tuple[str, ...]: Tuple of the unique letters from the puzzle.
    
    tuple_of_letters = ()
    for word in puzzle:
        for letter in word:
            if letter not in tuple_of_letters:
                tuple_of_letters += (letter,)
    return tuple_of_letters

def assign(letters, numbers_left, mapping, puzzle):
    # Finds a possible mapping for the puzzle given a sequence of alphabets within the puzzle and a sequence of numbers which we could match the alphabets to.
    # 
    # Args:
    #     letters (tuple[str, ...]): The letters that have yet to be allocated a mapping.
    #     numbers_left (tuple[int, ...]): The numbers that can be mapped to the letters.
    #     mapping (str): The current mapping that has been achieved.
    #     puzzle (tuple[str, ...]): Tuple of at least 2 elements, where the first (n - 1) elements are words to be added together, and the n-th element is the result that it should add up to.
    # 
    # Returns:
    #     str or bool: Returns deduced mapping if the above problem is solvable else returns False.
    
    if not letters:         # base case 1: possibly found a solution
        return check(puzzle, mapping)
    if not numbers_left:    # base case 2: an error
        return False
    curr_letter = letters[0]
    
    for i in range(len(numbers_left)):
        # assign a number in numers_left to the current letter
        # update it to a new map
        # need to keep the old map for use in the subsequent iterations
        dgt = numbers_left[i]
        map_copy = mapping[:]
        map_copy = mapping[:dgt] + curr_letter + mapping[dgt+1:]
        
        # call assign recursively, ensure that the size of the first argument 
        # (about letters waiting to be matched) has reduced, so the 
        # recursive call should terminate eventually
        res = assign(letters[1:], numbers_left, map_copy, puzzle) # fill in the arguments here

        # Check the result from the recursive call
        if res:
            return res
        # at this point here, it fails to find a solution with the
        # current mapping of number i to curr_letter; so ..
        # iterate to assign another number to the curr_letter

    # Exiting from the for-loop
    # going through all available numbers, fail to find a good mapping
    return False

def solve(puzzle):
    # Solves the puzzle provided, returning the corresponding mapping if the puzzle is solvable, and returning False if the puzzle is unsolvable.
    # 
    # Args:
    #     puzzle (tuple[str, ...]): Tuple of at least 2 elements, where the first (n - 1) elements are words to be added together, and the n-th element is the result that it should add up to.
    # 
    # Returns:
    #     str or None: Returns deduced mapping if the above problem is solvable else returns False.
    
    unique_letters_tup = unique_letters(puzzle)
    all_possible_numbers_left = tuple(range(10))
    empty_mapping = '.' * 10
    return assign(unique_letters_tup, all_possible_numbers_left, empty_mapping, puzzle)