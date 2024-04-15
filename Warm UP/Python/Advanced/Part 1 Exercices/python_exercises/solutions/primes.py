"""
See https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""


import sys
import time
import functools
import numpy as np
from prime import is_prime


def timed(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Elapsed time: {elapsed * 10 ** 3}ms")
        return res
    return wrapped


def get_number() -> int:
    try:
        num = int(sys.argv[1])
    except Exception as e:
        sys.exit(f"Something went wrong: {e}")
    return num


@timed
def prime_counter_naive(limit: int) -> int:
    limit = 10000 if limit > 10000 else limit   # Limit to 10000 to avoid excessive runtime
    primes = [is_prime(i) for i in range(limit + 1)]
    return sum(primes)


@timed
def prime_counter_set(limit: int) -> int:
    limit = 1000000 if limit > 1000000 else limit   # Limit to 1,000,000 to avoid excessive runtime
    potential_primes = set(range(2, limit + 1))
    for i in range(2, limit + 1):
        if i in potential_primes:
            not_primes = set(range(i * i, limit + 1, i))
            potential_primes -= not_primes
    return len(potential_primes)


@timed
def prime_counter_loop(limit: int) -> int:
    primes = [True if i > 1 else False for i in range(limit + 1)]
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i*i, limit, i):
                primes[j] = False
    return sum(primes)


@timed
def prime_counter_slice(limit: int) -> int:
    primes = np.ones(limit + 1, dtype=bool)
    primes[0:2] = False
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]: 
            primes[i*i:limit:i] = False
    return sum(primes)


if __name__ == "__main__":
    upper_bound = get_number()
    print(f"Computing number of primes from 0 to {upper_bound} ...")

    print("Naive computation (capped at 10,000):")
    print(prime_counter_naive(upper_bound))
    print("=" * 25)

    print("Sieve with loop and set (capped at 1,000,000):")
    print(prime_counter_set(upper_bound))
    print("=" * 25)

    print("Sieve with nested loop:")
    print(prime_counter_loop(upper_bound))
    print("=" * 25)

    print("Sieve with numpy:")
    print(prime_counter_slice(upper_bound))
