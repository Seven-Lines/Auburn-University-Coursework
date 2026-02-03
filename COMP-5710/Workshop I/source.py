def performMultiply(a, b):
    return a * b

def performDivision(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def performSquareRoot(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number.")
    return a ** 0.5