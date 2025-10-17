# Name: Pek Tze Hng, Zachary
# NUSNET ID: E1525681
# Question Number: 

# Define a Python function ds1(aString, n) which determines those characters that occur n times in aString.
# Function ds1() retuens a list of characters.

def ds1(aString, n):
    d = {}
    for c in aString:
        d[c] = d.get(c, 0) + 1

    result = []
    for k, v in d.items():
        if v == n:
            result.append(k)

    return result
