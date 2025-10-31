# Name: Pek Tze Hng, Zachary
# NUSNET ID: e1525681
# Question Number: 7

def fname(M):
    Mrows = len(M)
    Mcols = len(M[0])
    T = [[0] * Mcols for _ in range(Mrows)]

    for i in range(Mrows):
        for j in range(Mcols):
            T[i][j] = M[Mrows - 1 - i][j]

    return T
