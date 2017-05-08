def eval_poly(poly, x):       # x here is an x-coordinate
    total = 0.0
    index = 0.0
    for coefficient in poly:  # starts at 0 by default
        total += (x**index) * coefficient
        index += 1
    return total


sample = (0, 0, 5, 9.3, 7)
print(eval_poly(sample, -13))


def derive_poly(poly):
    if len(poly) < 2:
        return 0
    new = []
    index = 0
    for coefficient in poly[0:]:
        new.append(float(coefficient * index))
        index += 1
    return new


print(derive_poly(sample))


def newton_method(poly, x0, epsilon):
    root = x0
    if x0 == 0:
        root = .00001
    count = 0
    ddx = derive_poly(poly)
    while abs(eval_poly(poly, root)) >= epsilon:
        root = (root - eval_poly(poly, root) / eval_poly(ddx, root))
        count += 1
    return root, count


print(newton_method(sample, 1, .1))
