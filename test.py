# Basic arithmetic operations in Python

# Two example numbers
a = 15
b = 4

print("Operands: a =", a, ", b =", b)

# Addition
add_result = a + b
print("Addition (a + b):", add_result)  # 19

# Subtraction
sub_result = a - b
print("Subtraction (a - b):", sub_result)  # 11

# Multiplication
mul_result = a * b
print("Multiplication (a * b):", mul_result)  # 60

# True division (always returns float in Python 3)
div_result = a / b
print("Division (a / b):", div_result)  # 3.75

# Floor division (quotient rounded down)
floor_div_result = a // b
print("Floor Division (a // b):", floor_div_result)  # 3

# Modulus (remainder)
mod_result = a % b
print("Modulus (a % b):", mod_result)  # 3

# Exponentiation
exp_result = a ** b
print("Exponentiation (a ** b):", exp_result)  # 15^4 = 50625

# Mixed types: int and float
x = 7
y = 2.0
print("\nMixed types: x =", x, ", y =", y)
print("x / y =", x / y)       # 3.5 (float)
print("x // y =", x // y)     # 3.0 (still float because y is float)
print("x % y =", x % y)       # 1.0

# Unary plus and minus
print("\nUnary operators:")
print("+a =", +a)   # 15
print("-a =", -a)   # -15

# Grouping with parentheses
expr = (a + b) * (a - b)
print("\nExpression (a + b) * (a - b):", expr)  # (19) * (11) = 209

# Operator precedence example
# Exponentiation > multiplication/division > addition/subtraction
prec = 2 + 3 * 4 ** 2  # 2 + 3 * 16 = 2 + 48 = 50
print("Precedence example (2 + 3 * 4 ** 2):", prec)

# Safe division example to avoid ZeroDivisionError
def safe_divide(numerator, denominator):
    if denominator == 0:
        return "Cannot divide by zero"
    return numerator / denominator

print("\nSafe divide 10 by 0:", safe_divide(10, 0))
print("Safe divide 10 by 5:", safe_divide(10, 5))

# Bonus: using math functions
import math
print("\nMath helpers:")
print("abs(-5) =", abs(-5))                # absolute value
print("round(3.14159, 2) =", round(3.14159, 2))  # rounding to 2 decimals
print("math.sqrt(16) =", math.sqrt(16))    # square root
print("math.pow(2, 3) =", math.pow(2, 3))  # float exponentiation (2.0^3.0)
