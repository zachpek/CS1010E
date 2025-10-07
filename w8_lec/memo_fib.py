def memo_fib(n):
    results = {0: 0, 1: 1}
    def fib(n):
        if n < 0:
            raise ValueError('ur gay')
        elif n in results:
            return results[n]
        else:
            nth_value = fib(n - 1) + fib(n - 2)
            results[n] = nth_value
            return results[n]
    return fib(n)

def memo_fib_koklim(n):
    memo = {}
    def fib(k): # cool he used another variable to um take in the argument here (k instead of n), less confusing perhaps
        if k <= 1:
            return k
        elif k in memo:
            return memo[k]
        else:
            result = fib(k - 1) + fib(k - 2)
            memo[k] = result
            return result
    return fib(n)
