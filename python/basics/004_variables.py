# "004-Python-Variables-and-Data-Types"

#variables
# For reading: https://www.pythontutorial.net/python-basics/python-variables/

# Valid variable names
# Every variable should have a unique name
my_variable = "Hello"  # Contains only letters and underscore
myVariable123 = 42  # Contains letters, digits, and underscores
_variable = 3.14  # Starts with an underscore (valid but has special meaning)
MY_VAR = True  # Uppercase (case-sensitive)

# Case sensitivity
myVar = "Apple"
myvar = "Banana"

print(myVar)  # Output: Apple
print(myvar)  # Output: Banana (different from myVar)

# Invalid variable names (these would cause errors)
# 123variable = "Invalid"  # Starts with a digit (SyntaxError)
# my-variable = "Invalid"  # Contains a hyphen (SyntaxError)
# if = 10  # Uses a Python keyword (SyntaxError)


# Assigning values to variables
name = "Alice"  # String value
age = 25  # Integer value
height = 5.6  # Float value
is_student = True  # Boolean value

#output variable
print(name)
#print with format string
print(f"you are {name}")

# Assigning multiple variables in one line
x, y, z = 10, 20, 30
print(x, y, z)  # Output: 10 20 30

# Assigning the same value to multiple variables
a = b = c = 100
print(a, b, c)  # Output: 100 100 100

# Assigning different data types
message = "Hello, World!"  # String
pi_value = 3.14159  # Float
items_count = 42  # Integer
is_available = False  # Boolean

# Printing values
print(name, age, height, is_student)  # Output: Alice 25 5.6 True
print(message, pi_value, items_count, is_available)

# this is an expression
# 2+2

# this is a statement
# full_name = "John"

# you can assign function object and pretty much everything to a variable
my_print_function = print
my_print_function("This is my print function")