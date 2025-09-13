def alphabet_to_digit(c):
    # Convert an alphabet to its digit respresentation.
    # 
    # Args:
    #     c (str): Alphabet character.
    # 
    # Returns:
    #     int: Digit representation of the alphabet character.

    character_ordinal = ord(c)
    # condition c <= 'Z' is True when c is uppercase and False when c is lowercase
    return character_ordinal - ord('A') + 1 if c <= 'Z' \
        else character_ordinal - ord('a') + 1

def convert_prefix(prefix):
    # Converts the last two alphabets in a car licence plate prefix to their digit representation.
    # 
    # Args:
    #     prefix (str): The prefix of a car licence plate. This string must be non-empty.
    #
    # Returns:
    #     tuple[int, int]: A tuple of two integers, which are the converted digits of the last two alphabets in prefix

    number_of_zeros_to_prepend = 2 - len(prefix)
    converted_prefix = number_of_zeros_to_prepend * (0,) + tuple(map(alphabet_to_digit, prefix[-2:]))
    return converted_prefix

def convert_num_series(num_series):
    # Converts string of at most 4 digits to a tuple of integers with exactly 4 digits.
    # The integer 0 would be prepended to the tuple if the string has a length of less than 4.
    #
    # Args:
    #     num_series (str): The digits we want to pack into a tuple. This string has a maximum length of 4.
    #
    # Returns:
    #     tuple[int, int, int, int]: A tuple of 4 integers, consisting of the digits in num_series we want to pack into a tuple.

    number_of_zeros_to_prepend = 4 - len(num_series)
    converted_num_series = number_of_zeros_to_prepend * (0,) + tuple(map(int, num_series))
    return converted_num_series

def multiply_and_add_ho(multiplier):
    # Returns a function that multiplies each element of a tuple by each element of a specified multiplier tuple and returns their sum.
    # 
    # Args:
    #     multiplier (tuple[int, int, int, int, int, int]): A tuple of 6 integers used as multipliers in the function returned.
    #
    # Returns:
    #     Callable[[tuple[int, int, int, int, int, int]], int]: A function that takes a tuple of 6 integers, multiplies each number of the tuple by the corresponding number of the same index in the 'multiplier' tuple, and returns the sum of the products.

    def multiply_series(series):
        # Multiplies each number in the series by the corresponding number in the 'multiplier' tuple specified in the outer scope.
        # 
        # Args:
        #     series (tuple[int, int, int, int, int, int]): A tuple of 6 integers to be multiplied.
        # 
        # Returns:
        #     int: Sum of product of 'series' and 'multiplier'.
        
        multiplied_series = map(lambda i: multiplier[i] * series[i], range(len(multiplier)))
        return sum(multiplied_series)
    return multiply_series

def remainder_to_checksum_letter(remainder):
    # Takes an integer checksum remainder and returns the corresponding checksum letter in uppercase.
    #
    # Args:
    #     remainder (int): checksum remainder.
    #
    # Returns:
    #     str: uppercase checksum letter

    checksum_letters = ('A', 'Z', 'Y', 'X', 'U', 'T', 'S', 'R', 'P', 'M', 'L', 'K', 'J', 'H', 'G', 'E', 'D', 'C', 'B') 
    corresponding_checksum_letter = checksum_letters[remainder]
    return corresponding_checksum_letter

def checksum_calculator_ho(multiplier):
    # Returns a function that computes the checksum of a car licence plate based on a multiplier.
    #
    # Args: 
    #     multiplier (tuple[int, int, int, int, int, int]): A tuple of 6 integers used as multipliers in the function returned.
    #
    # Returns:
    #     Callable[[str], str]: A function that takes a car licence plate string and returns the corresponding checksum.

    def compute_checksum(plate):
        # Computes the checksum of a car licence plate based on the 'multiplier' tuple specified in the outer scope.
        # The 7 computation steps are outlined in page 2 of the assignment handout.
        #
        # Args:
        #     plate (str): The car licence plate.
        # 
        # Returns:
        #     str: The corresponding checksum.
        
        is_alphabet = lambda character: ord(character) >= ord('A')
        is_number = lambda character: ord(character) < ord('A')

        prefix = tuple(filter(is_alphabet, plate))
        numbers = tuple(filter(is_number, plate))

        prefix_series = convert_prefix(prefix)
        num_series = convert_num_series(numbers)

        combined_series = prefix_series + num_series

        multiply_series = multiply_and_add_ho(multiplier)
        sum_of_multiplied_series = multiply_series(combined_series)

        remainder = sum_of_multiplied_series % 19

        return remainder_to_checksum_letter(remainder)
    return compute_checksum