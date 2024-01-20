'''Memoization is a way of having your recursive functions
memorize the results of all new computations your functions
encounter by the use of hash tables. This drasticly reduces
the speed of your algorithms...Making an implementation
of it below.
'''

def fib (n, memo):
    '''memoization implemented for the Fibonacci Sequence.
    n is the inputted number, memo is the hash table storing
    computational results
    '''

    if n == 0 or n == 1:
        return n

    # check the hash table (called memo) to see whether fib(n)
    # was already computered or not:
    memo[n] = fib(n - 2, memo) + fib(n - 1, memo)

    # By now, fib(n)'s result is certainly in memo. (Perhaps it was
    # there before, or perhaps we just stored it there in the previous
    # line of code. But it's certainly there now...So let's return it)

    return memo[n]

print(fib(6, {}))
