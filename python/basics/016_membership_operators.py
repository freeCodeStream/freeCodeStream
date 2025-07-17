# Membership operators
# They are used to test whether a value or variable is found in a sequence (like string, list, tuple, set, or dictionary)
# Operators: 'in' and 'not in'


# 1. Check if a product is available in a store
available_products = ["apple", "banana", "milk", "bread"]

print("milk" in available_products)        # True
print("eggs" not in available_products)     # True

# 2. Check if a username is already taken
existing_usernames = ["john_doe", "alice99", "data_wizard"]

new_user = "john_doe"
print(new_user in existing_usernames)       # True

# 3. Check if a character is in a password
password = "SuperSecure123"
print("S" in password)                      # True
print("x" not in password)                  # True

# 4. Check if a city is in the delivery zone
delivery_cities = {"New York", "Los Angeles", "Chicago"}  # using a set for fast lookup
print("Chicago" in delivery_cities)        # True
print("Boston" in delivery_cities)         # False

# 5. Check if a key exists in a dictionary (like a user database)
user_profiles = {
    "alice": {"age": 30, "role": "analyst"},
    "bob": {"age": 24, "role": "data scientist"}
}

print("alice" in user_profiles)             # True
print("eve" not in user_profiles)           # True

# -------------------------------
# Weird Situations / Edge Cases
# -------------------------------

# 1. Case sensitivity in strings
print("apple" in "Apple Pie")               # False (Python is case-sensitive)

# 2. Membership in numbers (not iterable)
# print(3 in 12345)                         # TypeError: argument of type 'int' is not iterable


# 3. Membership in nested data structures
student_courses = {
    "john": ["math", "science"],
    "mary": ["history", "math"]
}

# Check if "math" is in any student's course list
is_math_enrolled = any("math" in courses for courses in student_courses.values())
print(is_math_enrolled)                    # True

# 4. Checking for substring vs word
sentence = "I love apple pie"
print("apple" in sentence)                 # True
print("app" in sentence)                   # True (substring)
print("apple pie" in sentence)             # True
print("pie apple" in sentence)             # False


# 5. Using 'in' with None

# print("x" in None)                       # TypeError: argument of type 'NoneType' is not iterable

# 6. Using 'in' with booleans
print(True in [0, 1, 2])                   # True (True == 1)
print(False in [0, 1, 2])                  # True (False == 0)
