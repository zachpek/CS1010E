import random

def print_society(society) :
    '''
    Pretty prints a given society.

    Parameters:
        society (list): The society to be printed.
    '''
    print('\n'.join([' '.join(row) for row in society]))

def build_society(m, n) :
    '''
    Builds an m by n society randomly assigned with * and -

    Parameters:
        m (int): The number of rows of the society.
        n (int): The number of columns of the society.

    Returns:
        the resulting randomly built society.
    '''
    society = [random.choices(['*', '-'], k=n) for _ in range(m)]
    return society

def model_society(txt):
    # Takes in prettily formatted str of a society and returns that society represented as an array
    
    split_by_newline = txt.split('\n')
    return [row.split(' ') for row in split_by_newline if row != '']
