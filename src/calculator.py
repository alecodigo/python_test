def sum(a, b):
    """
    >>> sum(5,7)
    12
    """
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    """
    >>> divide(10, 0)
    >>> divide(10, 10)
    """
    if b == 0:
        raise ValueError('No esta permitida la division por 0.')
    return a / b

