import math


def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be 0 for a quadratic equation.")

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root, root
    else:
        return None

print(solve_quadratic(1, -3, 2))