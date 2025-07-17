"""
Python Identity Operators:
--------------------------
They compare the memory locations of two objects to check if they are actually the same object (not just equal in value).

Operators:
- is
- is not

Real-life analogy:
Think of 'is' like asking "Are these two people the same person?" not "Do they look the same?"
"""

# Example 1: Comparing two employee records (same object or not?)
employee_record_1 = {"name": "Alice", "id": 101}
employee_record_2 = employee_record_1  # both variables point to the same dictionary object

print("Example 1:")
print(f"employee_record_1 is employee_record_2: {employee_record_1 is employee_record_2}")  # True
print(f"employee_record_1 == employee_record_2: {employee_record_1 == employee_record_2}")  # True (values are equal)

print("\n--------")

# Example 2: Two different employee records with same data
employee_record_3 = {"name": "Alice", "id": 101}  # new dictionary with same data as employee_record_1

print("Example 2:")
print(f"employee_record_1 is employee_record_3: {employee_record_1 is employee_record_3}")  # False (different objects)
print(f"employee_record_1 == employee_record_3: {employee_record_1 == employee_record_3}")  # True (values equal)

print("\n--------")

# Example 3: Comparing string literals from a login system
user_input_username = "admin"
stored_username = "admin"

print("Example 3:")
print(f"user_input_username is stored_username: {user_input_username is stored_username}")  # True or False depending on interning
print(f"user_input_username == stored_username: {user_input_username == stored_username}")  # True

print("\n--------")

# Example 4: Comparing numbers
a = 256
b = 256

print("Example 4:")
print(f"a is b: {a is b}")  # True (small integers are cached in Python)
print(f"a == b: {a == b}")  # True

c = 257
d = 257

print(f"c is d: {c is d}")  # Usually False (integers > 256 are not cached)
print(f"c == d: {c == d}")  # True

print("\n--------")

# Weird situations / edge cases:

print("Weird Cases:")

# 1. Identity with immutable vs mutable objects
num1 = 1000
num2 = 1000
print(f"num1 is num2: {num1 is num2}")  # False usually

str1 = "hello_world"
str2 = "hello_" + "world"
print(f"str1 is str2: {str1 is str2}")  # True due to string interning

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"list1 is list2: {list1 is list2}")  # False (different lists)

# 2. Using 'is' for None checks (recommended)
some_variable = None
print(f"some_variable is None: {some_variable is None}")  # True

# 3. Using 'is' with booleans
x = True
y = 1
print(f"x is y: {x is y}")  # False, True is bool, 1 is int, different objects
print(f"x == y: {x == y}")  # True, because bool subclass of int and value is equal

# 4. Comparing floats with 'is' (not recommended)
f1 = 3.14
f2 = 3.14
print(f"f1 is f2: {f1 is f2}")  # Usually False, because floats are not cached
