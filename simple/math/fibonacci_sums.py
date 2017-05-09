from sys import argv


def fibonacci_sums(max_sum):
    sum = 2
    a, b = 1, 2
    while b < max_sum:
        a, b = b, a + b
#       if b % 2 == 0:    # not sure what I was doing here, why would it need to be even?
        sum += b
    print(sum)


if __name__ == "__main__":
    try:
        fibonacci_sums(int(argv[1]))
    except (ValueError, IndexError):
        fibonacci_sums(4000000)
