# ZeroDivisionError :
a = 5
b = 2
try:
    print("open")
    print(a / b)
except Exception as e:
    print("you cannot divide by zero.", e)
finally:
    print("Close")

"""
Exception - Base class for all exceptions.
ArithmeticError - Base class for errors related to arithmetic operations.
ZeroDivisionError - Division by zero.
OverflowError - Operation exceeds the limits of numeric types.
IndexError - Index is out of range for a list or other sequence.
KeyError - Dictionary key is not found.
ValueError - Incorrect value is passed to a function.
TypeError - Unsupported operation or type mismatch.
FileNotFoundError - File cannot be found.
NameError - Variable or function name is not defined.
AttributeError - Attribute is not found on an object.
ImportError - Module cannot be imported.
StopIteration - Raised when an iterator is exhausted.
MemoryError - Memory allocation failure.
OSError - System-related errors (e.g., file access, I/O errors).
TimeoutError - Operation timed out.
"""