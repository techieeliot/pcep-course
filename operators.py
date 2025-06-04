# operators = {
#     "arithmetic": ["+", "-", "*", "/", "//", "%", "**"],
#     "comparison": ["==", "!=", "<", ">", "<=", ">="],
#     "logical": ["and", "or", "not"],
#     "assignment": ["=", "+=", "-=", "*=", "/=", "//=", "%=", "**="],
#     "bitwise": ["&", "|", "^", "~", "<<", ">>"],
#     "identity": ["is", "is not"],
#     "membership": ["in", "not in"]
# }
# Operators in Python are special symbols that perform operations on variables and values.
# They can be categorized into different types based on their functionality.
def arithmetic_operations(a, b):
    return {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b,
        "floor_division": a // b,
        "modulus": a % b,
        "exponentiation": a ** b
    }

def comparison_operations(a, b):
    return {
        "equal": a == b,
        "not_equal": a != b,
        "less_than": a < b,
        "greater_than": a > b,
        "less_than_or_equal": a <= b,
        "greater_than_or_equal": a >= b
    }

def logical_operations(a, b):
    return {
        "and": a and b,
        "or": a or b,
        "not": not a
    }

def assignment_operations(a, b):
    a += b
    b -= a
    return {
        "assignment": a,
        "addition_assignment": a + b,
        "subtraction_assignment": a - b,
        "multiplication_assignment": a * b,
        "division_assignment": a / b,
        "floor_division_assignment": a // b,
        "modulus_assignment": a % b,
        "exponentiation_assignment": a ** b
    }

def bitwise_operations(a, b):
    return {
        "bitwise_and": a & b,
        "bitwise_or": a | b,
        "bitwise_xor": a ^ b,
        "bitwise_not": ~a,
        "left_shift": a << 1,
        "right_shift": a >> 1
    }

# PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
def precedence_operations(a, b):
    return {
        "parentheses": (a + b) * (a - b),
        "exponentiation": a ** b,
        "multiplication_division": a * b / 2,
        "addition_subtraction": a + b - 1
    }

