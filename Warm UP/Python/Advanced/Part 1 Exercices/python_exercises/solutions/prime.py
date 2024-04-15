import sys 


def _get_number() -> int:
    try:
        num = int(sys.argv[1])
        return num
    except ValueError as e:
        sys.exit(f"bad input: {e}")


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def run() -> None:
    num = _get_number()
    print(is_prime(num)) 


if __name__ == "__main__": 
    run()
