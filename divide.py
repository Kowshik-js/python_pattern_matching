def divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("Divisor cannot be zero")
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
    dividend, divisor = abs(dividend), abs(divisor)
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    return sign * quotient
numerator = 10
denominator = 3
result = divide(numerator, denominator)
print(f"{numerator} divided by {denominator} is {result}")
