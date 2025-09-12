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
    #     num_series (str): The digits we want to pack into a tuple. Thhis string has a maximum length of 4.
    #
    # Returns:
    #     tuple[int, int, int, int]: A tuple of 4 integers, consisting of the digits in num_series we want to pack into a tuple.

    number_of_zeros_to_prepend = 4 - len(num_series)
    num_series = number_of_zeros_to_prepend * '0' + num_series
    return tuple(map(int, num_series))

def multiply_and_add_ho(multiplier):
    def um_something(series):
        pass