def divide(dividend, divisor):
    """
    :param dividend: a numerical value
    :param divisor:  a numerical
    :return: a numerical value if division is possible. Otherwise, None
    """
    quotient = None
    if divisor is not None :
        if divisor != 0:
            quotient = dividend / divisor
    return quotient