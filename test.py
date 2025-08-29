def add2(x):
    return lambda y: x + y

def alt3(x, y):
    return add2(x)(y) if x % 10 == 1 \
        else add2(x)(-y)

print(alt3(2918, 3))
print(alt3(271,10))