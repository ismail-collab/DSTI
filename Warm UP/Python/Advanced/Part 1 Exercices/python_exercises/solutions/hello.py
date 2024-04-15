import sys


def run() -> None:
    if len(sys.argv) > 1:
        print(f"hello, {sys.argv[1]}")
    else:
        print("hello, world")


if __name__ == "__main__":
    run()
