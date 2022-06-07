import math


def trapezoidal(f, a, b, n):
    # spacing
    h = (b - a) / n

    # Approximation of the trapezoidal method for integral calculation
    result = 0
    i = 0
    while i < n:
        b = a + h
        s = (f(a) + f(b))
        result += 0.5 * (b - a) * s
        a = b
        i += 1
    return result


def calculate_amount_of_sections(value, a, b, error_range):
    return int(math.sqrt(((b - a) ** 3 * value) / (12 * error_range)) + 1)









