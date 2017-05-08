def sum_squares(x):
    sum = 0
    for y in range(1, x + 1):
        sum += y**2
    print(sum)
    return(sum)


def square_sums(x):
    sum = 0
    for y in range(1, x + 1):
        sum += y
    print(sum**2)
    return(sum**2)


def sum_square_difference(x):
    print(square_sums(x) - sum_squares(x))


if __name__ == "__main__":
    sum_square_difference(10)
