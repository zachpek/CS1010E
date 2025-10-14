def zero_matrix(rows, cols):
    # BIG ISSUE
    # THE INSIDE LIST IS DUPLICATED rows TIMES
    # SO MODIFYING AN ELEMENT IN THAT INNER LIST WOULD DO SO rows TIMES, ONCE FOR EACH ROW
    return [[0] * cols] * rows

def zero_matrix_revised(rows, cols):
    return [[0] * cols for _ in range(rows)]

def zero_matrix_koklim(rows, cols):
    M = []

    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(0)
        M.append(row)

    return M

def zero_matrix_list_compre_koklim(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def mat_ascending(rows, cols):
    # um just no: return [cols * r + c for c in range(cols) for r in range(rows)]
    # lol returns a 1-D array: return [cols * r + c for r in range(rows) for c in range(cols)]
    # order is wrong: return [[cols * r + c for r in range(rows)] for c in range(cols)]
    return [[cols * r + c for c in range(cols)] for r in range(rows)] # builds a list row by row

def deep_copy(M):
    result = []
    
    for elem in M:
        if type(elem) == list:
            result.append(deep_copy(elem))
        else:
            result.append(elem)

    return result

def mat_add(A, B):
    # result = A.copy() # or result = [row for row in A] # breaks for dimensions greater than 2
    # koklim: [row.copy() for row in A]
    result = deep_copy(A)
    for row in B: # lol rip this doesnt allow for matrices which aren't 2-D
        for col in row:
            result[row][col] += B[row][col]
    return result

def mat_add_koklim(A, B):
    n_rows = len(A)
    n_cols = len(A[0])

    return [[A[r][c] + B[r][c] for c in range(n_cols)] for r in range(n_rows)]

def mat_mult_3x3(A, B):
    M = [[0] * 3 for _ in range(3)]
    
    for r in range(3):
        for c in range(3):
            M[r][c] = sum([A[r][k] * B[k][c] for k in range(3)])
    return M

def submat(M, r1, r2, c1, c2):
    return [[M[r][c] for c in range(c1, c2 + 1)] \
            for r in range(r1, r2 + 1)]
