import math

# Sieve of Eratosthenes
def sieve_of_eratosthenes(n):
    primes = list(range(2,n+1))

    i=2
    while (i <= int(math.sqrt(n))):
        if i in primes:
            for num in range(i*2,n+1,i):
                if num in primes:
                    primes.remove(num)
        i = i+1
    print (primes)
