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

def gol(cell_value, live_neigh) : 
    # Returns True or False for whether the cell of the given cell_value (a boolean) will be alive in the next round given the number of live neighbours around it
    if not cell_value:
        if live_neigh == 3:
            return True
        return False
    
    if live_neigh in (2, 3):
        return True
    return False

def tabulate(rules):
    live_results = ['live' if rules(True, live_neigh) else 'dead' for live_neigh in range(9)]
    dead_results = ['live' if rules(False, live_neigh) else 'dead' for live_neigh in range(9)]
    return [('live', live_results),
            ('dead', dead_results)]
            
def destiny(society, coordinates, gol) :
    '''
    Determines the liveliness of the cell in coordinates in the next generation.

    Parameters:
        society      (list): The society.
        coordinates (tuple): The tuple representing the coordinates whose
                             destiny is to be determined.
        gol                : The game-of-life rules

    Returns:
        the cell's destiny.
    '''
    n_rows, n_cols = len(society), len(society[0])
    selected_r, selected_c = coordinates
    cell_value = True if society[selected_r][selected_c] == '*' else False
    
    live_neigh = 0
    for r in (selected_r - 1, selected_r, selected_r + 1):
        for c in (selected_c - 1, selected_c, selected_c + 1):
            if r >= 0 and c >= 0 and r < n_rows and c < n_cols and (r, c) != (selected_r, selected_c):
                if society[r][c] == '*':
                    live_neigh += 1
    
    return '*' if gol(cell_value, live_neigh) else '-'

def evolve(society, n, gol) :
    '''
    Evolves the society by n iterations given the rules in Game Of Life.

    Parameters:
        society (list): The society to be evolved.
        n        (int): The number of evolutions to perform.
        gol           : A function encoding game-of-life rules

    Returns:
        a tuple consisting of the
            (1) resulting society
            (2) number of evolutions before arriving at stability.
    '''
    def evolve_society(society, n, gol):
        if n <= 0:
            return society, n
        evolved_society = [[destiny(society, (r, c), gol) for c in range(len(society[0]))] \
                           for r in range(len(society))]
        if evolved_society == society:
            return society, n
        return evolve_society(evolved_society, n - 1, gol)
    
    resulting_soc, last_n = evolve_society(society, n, gol)
    return resulting_soc, n - last_n

def migrate(society) :
    '''
    Causes a society to migrate based on the population census.

    Parameters:
        society (list): The given society.

    Returns:
        the resulting society after migration.
    '''
    n_rows = len(society)
    count_per_row = []
    resulting_soc = []
    
    for r in range(n_rows):
        count_per_row.append((society[r].count('*'), r))
    count_per_row.sort(key=lambda pair: pair[0], reverse=True)
    
    for _, r_to_insert in count_per_row:
        resulting_soc.append(society[r_to_insert])
        
    return resulting_soc
