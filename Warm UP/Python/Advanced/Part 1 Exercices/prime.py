import sys
import time
import datetime

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python prime.py <number>")
    else:
        try:
            number = int(sys.argv[1])
            start_time = datetime.datetime.now()
            result = is_prime(number)
            print(number, "Is prime :",result)
            end_time= datetime.datetime.now()
            complexity = start_time - end_time
            print(complexity.microseconds,"ms")
        except ValueError:
            print("Please provide a valid integer.")
