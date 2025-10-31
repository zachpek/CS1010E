def transpose_no_lc(M):
    Mrows = len(M)
    Mcols = len(M[0])
    T = [[0] * Mrows for r in range(Mcols)]

    for i in range(Mcols):
        for j in range(Mrows):
            T[i][j] = M[j][i]
        
    return T

def transpose_lc(M):
    Mrows = len(M)
    Mcols = len(M[0])

    T = [[M[j][i] for j in range(Mrows)] for i in range(Mcols)]

    return T

def mat_mult(A, B):
    rows = len(A)
    cols = len(B[0])
    n = len(B) # = cols of A = rows of B

    M = [[sum([A[i][k] * B[k][j] for k in range(n)]) for j in range(cols)] for i in range(rows)]
    
    return M

def minor_mat(M, r, c):
    S = []

    for i in range(len(M)):
        if i != r:
            S.append(M[i][:c] + M[i][c + 1:])

    return S

def minor_mat_khoo(M, r, c):
    S = []

    for row in M[:r] + M[r + 1:]:
        S.append(row[:c] + row[c + 1:])

    return S

def submat_sums(M, srows, scols):
    Mrows = len(M)
    Mcols = len(M[0])
    Trows = Mrows // srows # result matrix rows
    Tcols = Mcols // scols # result matrix columns
    T = [ [0] * Tcols for r in range(Trows) ] # result matrix

    for i in range(Mrows):
        for j in range(Mcols):
            T[i // srows][j // scols] += M[i][j]
    
    return T