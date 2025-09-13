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
    # A higher order function which returns a function which takes a sequence and multiplies each element of the sequence.
    #
    # Args:
    #     multiplier (tuple[int, int, int, int, int, int]): Specifies by what factor to multiply each element of a series.
    #
    # Returns:
    #     Callable[[tuple[int, int, int, int, int, int]], int]: A function which takes a sequence and multiplies each element of the sequence by the corresponding integer of the same index in the "multiplier" argument.
    def multiply_series(series):
        multiplied_series = map(lambda i: multiplier[i] * series[i], range(len(multiplier)))
        return sum(multiplied_series)
    return multiply_series

def remainder_to_checksum_letter(remainder):
    # 
    #
    # Args:
    #     remainder (int):
    #
    # Returns:
    #     str:

    return

def checksum_calculator_ho(multiplier):
    #
    #
    # Args: 
    #     multiplier (tuple[int, int, int, int, int, int])
    #
    # Returns:
    #     Callable[[tuple[int, int, int, int, int, int]], int]:

    
    def compute_checksum(plate):
        return
    return compute_checksum