def is_prime(n):
    return not any(map(lambda i: n % i == 0, range(2, n)))

lambda_is_prime = lambda n: any(map(lambda i: n % i == 0, range(2, n)))

# ok actually this is wrong because n <= 1 returns true

def is_prime(n):
    return n > 1 and not any(map(lambda i: n % i == 0, range(2, n)))

# and now lecture solution

def is_prime_lecture(n):
    return n > 1 and \
    all(map(lambda i: n % i != 0, range(2, n)))
    # all(map(lambda i: n % i != 0, range(2, int(sqrt(n)) + 1)))