def check(puzzle, mapping):
    # Checks if a given mapping is valid.
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

    mapping_letters = ''
    for letter in mapping:
        if letter != '.':
            if letter in mapping_letters:
                return False
            if letter not in puzzle_letters:
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
    pass