def find_primes_120(n):
    # find primes from 0 to 120
    # only need to test with prime numbers ≤ sqrt(120) = 10.95 given in the below list
    # 11 ** 2 = 121 onwards cannot - would miss numbers divisible by 11 121 and beyond
    prime_tests = [2, 3, 5, 7]
    # nonprime = [i for i in range(4, n + 1) if (i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0) and i not in (5, 7)]
    # nonprimes = [i for i in range(4, n + 1) if any(map(lambda n: i % n == 0, prime_tests)) and i not in prime_tests]
    nonprimes = [i for i in range(4, n + 1) if any(i % n == 0 for n in prime_tests) and i not in prime_tests]
    # ^^^ functions 'all' and 'any' take in iterables which can be specified just like that in list comprehensions
    print(f'nonprimes: {nonprimes}')
    prime = [i for i in range(2, n + 1) if i not in nonprimes]
    return prime

def find_primes(n):
    prime_tests = range(2, int(n ** 0.5) + 1) 
    nonprimes = [j for i in prime_tests for j in range(i * 2, n + 1, i)]
    print(f'nonprimes: {nonprimes}')
    return [x for x in range(2, n + 1) if x not in nonprimes]

def find_primes_more_efficient_maybe(n):
    # ok Gemini said no but I'll take this as prac (im gna crash out)
    prime_tests = find_primes(int(n ** 0.5))
    print(f'prime tests: {prime_tests}')
    nonprimes = [i for i in range(4, n + 1) if any(i % n == 0 for n in prime_tests) and i not in prime_tests]
    print(f'nonprimes: {nonprimes}')
    prime = [i for i in range(2, n + 1) if i not in nonprimes]
    return prime

def find_primes_khoo(n):
    nonprime = [j for i in range(2, 8) for j in range(i * 2, n, i)]
    # prime = [x for x in range(1, n + 1) if x not in nonprime] # lol sike 1 isn't a prime number
    prime = [x for x in range(2, n + 1) if x not in nonprime] # khoo just returned this
    return prime

def find_primes_khoo_efficient(n):
    nonprimes = []
    [nonprimes.append(j) for i in range(2, int(n ** 0.5) + 1) \
        if i not in nonprimes for j in range(i * 2, n + 1, i)]
    # Google: the above isn't pythonic (and it's equivalent to the below:)
    # nonprimes = []
    # for test in range(2, int(n ** 0.5) + 1):
    #     if test not in nonprimes: # if test is not a prime number, all multiples of it have already been captured in nonprimes list (e.g., for 4, every one of its multiples up to n have been captured)
    #         for np in range(test * 2, n + 1, test):
    #             nonprimes.append(np)
    # return nonprimes
    return [p for p in range(2, n + 1) if p not in nonprimes]

def find_primes_gemini(n):
    """
    Finds all prime numbers up to a limit n using only list comprehension.
    Assumes n >= 2.
    """
    # 1. Generate a list of numbers from 2 up to and including n.
    # 2. Filter this list: a number 'i' is prime if no number 'j' 
    #    in the range [2, i-1] divides 'i' evenly.
    return [i for i in range(2, n + 1) if all(i % j != 0 for j in range(2, int(i**0.5) + 1))]
