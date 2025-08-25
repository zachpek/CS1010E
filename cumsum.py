from functools import reduce

# Write a function cumulative_sum that takes in a sequence
# {a, b, c, . . . }, and returns {a, a + b, a + b + c, . . . }

# model answer (i just realised can use sum instead of reduce(lambda x,y:x+y, iterable))

# first, generate the sub-sequences
def cumulative_sum(seq):
    return tuple(map(lambda i: seq[:i + 1], range(len(seq))))

def cumulative_sum(seq):
    return tuple(map(lambda i: sum(seq[:i + 1]), range(len(seq))))

# my attempts

def tups_long(seq):
    tups = ()
    for i in range(len(seq)):
        tups += (seq[:i+1],)
    return tups

def tups(seq):
    return tuple(map(lambda i: seq[:i + 1], range(len(seq))))

tups_lambda = lambda seq: tuple(map(lambda i: seq[:i + 1], range(len(seq))))

def join_long(tups):
    result = ()
    for i in range(len(tups)):
        result += (reduce(lambda x, y: x + y, tups[i]),)
    return result

def join(tups):
    return tuple(map(lambda i: reduce(lambda x, y: x + y, tups[i]), range(len(tups))))

join_lambda = lambda tups: tuple(map(lambda i: reduce(lambda x, y: x + y, tups[i]), range(len(tups))))

def cumsum(seq):
    return join_long(tups_long(seq))

cumsum_lambda = lambda seq: join_lambda(tups_lambda(seq))

cumsum_lambdalambda = lambda seq: join_lambda(tuple(map(lambda i: seq[:i + 1], range(len(seq)))))

cumsum_lambdalambdalambda = lambda seq: tuple(map(lambda i: reduce(lambda x, y: x + y, tuple(map(lambda i: seq[:i + 1], range(len(seq))))[i]), range(len(tuple(map(lambda i: seq[:i + 1], range(len(seq))))))))
# ^ doesn't follow DRY: tuple(map(lambda i: seq[:i + 1], range(len(seq)))) is repeated

# oh wait i could've applied the reduce/sum function to the sliced sequence right away

cumsum_revised = lambda seq: tuple(map(lambda i: reduce(lambda x, y: x + y, seq[:i + 1]), range(len(seq))))

s = tuple('string')
n = tuple(range(1,6))

print(cumsum_revised(s), cumsum_revised(n), sep='\n'*2)