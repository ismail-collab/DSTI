import sys 


def get_nums() -> list[int]:
    try:
        args = [int(arg) for arg in sys.argv[1:]]
    except ValueError as e:
        sys.exit(f"bad input: {e}")
    return args


def get_sum(args: list[int]) -> int:
    return sum(args)


def run() -> None:
    nums = get_nums()
    print(get_sum(nums))


if __name__ == "__main__":
    run()
