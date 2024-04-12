"""
Identifying Prime Numbers

REQUIREMENTS:
- Only one integer value is accepted as an argument
- The script does not crash if a non-integer is provided
- The script returns an integer value with the total count of prime numbers
  from 1 up to and including the number provided
"""
import sys
import time
import functools
import numpy as np

### This is how we make a decorator
def timer(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        start_time = time.perf_counter()
        res = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Execution Time: {elapsed_time} seconds.")
        return res
    return wrapped

def parse_input(input_value: str) -> int:
    """
    This function will parse a given input into an integer.

    If the string provided cannot be converted to an integer,
    the output value will be -1
    """
    try:
        converted_input = int(input_value)

        # Additionally check to make sure that the number is not a float
        if converted_input != float(converted_input) or converted_input < 1:
            converted_input = -1
    except ValueError:
        converted_input = -1
    
    return converted_input

@timer
def count_primes_by_sieve(max_num: int) -> int:
    """
    Implements the Sieve of Eratosthenes Algorithm
    """
    # Create the list of truth values
    primes_bools = [True for _ in range(max_num +1)]

    # Go through each number starting with the first prime, 2
    current_num = 2
    while(current_num ** 2 <= max_num):
        # If the current num is still true in the list, then it's prime
        if(primes_bools[current_num]):

            # Update all multiples since they can be factored by a prime
            for i in range(current_num ** 2, max_num + 1, current_num):
                primes_bools[i] = False

        # Update the current number
        current_num += 1
            
    return sum(primes_bools) - 2

@timer
def count_primes_by_sieve_numpy(max_num: int) -> int:
    """
    This function will count primes from 1 until a specified number
    We will implement the  Sieve of Eratosthenes Algorithm
    Additionally, we will use numpy for speed
    """
    # Create the list of truth values
    primes_bools = np.array([True for _ in range(max_num +1)])

    # Go through each number starting with the first prime, 2
    current_num = 2
    while(current_num ** 2 <= max_num):
        # If the current num is still true in the list, then it's prime
        if(primes_bools[current_num]):

            # Update all multiples since they can be factored by a prime

            # In this case we index starting at the square of the current number
            # stepping by the current number
            primes_bools[current_num ** 2::current_num] = False
            # array_name[start_pos:end_pos:step_size] -- Example for the indexing above

        # Update the current number
        current_num += 1
        print(current_num)
            
    return sum(primes_bools) - 2


if __name__ == '__main__':
    # Capture User Input and make sure it's valid
    user_input = sys.argv
    is_valid_input = len(user_input) == 2

    if not is_valid_input:
        print("Exactly one input must be provided")
    else:
        input_numeric = parse_input(user_input[1])
        if input_numeric == -1:
            print("Provided input must be a positive integer greater than 1")
        else:
            prime_count = count_primes_by_sieve_numpy(input_numeric)
            print(f"There are {prime_count} prime numbers from 1 to {input_numeric}.")
