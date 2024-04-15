# Getting Started with Python

These exercises are meant to be completed as single-file Python programs.

Prerequisites:

- A text editor to write your programs, recommended is [vscode](https://code.visualstudio.com/)
- A Python interpreter from [python.org](https://python.org), recommended is version 3.11
- A terminal to run text-based commands, recommended is [Windows terminal](https://apps.microsoft.com/detail/9n0dx20hk701)


If you are not sure if Python is available on your system or what version is
installed, open your terminal app and type:

```
python --version
```

## Hello, World!

Write a Python program called `hello.py` that prints `hello, world` when run.

```
> python ./hello.py
> hello, world
```

## Hello, you!

Expand your first program so that it behaves as follows:

- If you run the program with no argument, it prints `hello, world!`
- If you run the program with an argument, it prints `hello, <argument>`

```
> python ./hello.py albert
> hello, albert
```

## Simple Addition

Write a Python program called `add.py` that takes two integers as arguments and
prints the sum of the two integers when run.

```
> python ./add.py 1 2
> 3
```

- Bonus 1: Your program can take any number of input arguments
- Bonus 2: Your program gives an error but does not crash on invalid input

## Prime Time

Write a program called `prime.py` that takes a positive integer as argument and
prints `true` when the integer is a prime number, else `false`.

```
> python ./prime.py 3
> true
```
```
> python ./prime.py 6
> false
```

- Bonus: Find a way to measure the time it takes your program to compute if your number is a prime (hint: Use timeit or 
your own decorator).

```
> python ./prime.py 3
> true
> Runtime: 00:00:01
```

## Prime Time^2

Write a new program `primes.py` that takes a positive integer as argument and then prints the number of prime numbers
between 0 and that number.

```
python ./primes.py 100
25
```

_Note: To run the provided example solution, you must install _`numpy`_ in your environment_
