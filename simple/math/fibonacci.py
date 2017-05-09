from sys import argv


def fibonacci(n, *option):
    t, a, b = 0, 0, 1
    if option == ():
        while t < n:
            a, b = b, a + b
            t += 1
        print(a)
    elif ('all' in option):
        while t < n:
            print(a)
            a, b = b, a + b
            t += 1
        print(a)
    else:
        print("You entered an option that is not available.\nOptions: 'all'")


if __name__ == "__main__":
    try:
        fibonacci(int(argv[1]))
    except IndexError or ValueError:
        fibonacci(10)
