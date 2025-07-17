# Introduction to Comparison Operators;
# Comparison operators are used to compare two values.
# They return either True or False.
# Comparison operators: ==, !=, >, <, >=, <=

# comparison_operators.py

# ------------------------------
# Comparison Operators Examples
# ------------------------------

print("\n# Real-life examples with comparison operators")

# 1. Less than (<)
customer_age = 16
legal_driving_age = 18
print("Is the customer too young to drive?", customer_age < legal_driving_age)  # True

# 2. Less than or equal to (<=)
exam_score = 70
passing_score = 70
print("Did the student pass the exam?", exam_score >= passing_score)  # True

# 3. Greater than (>)
salary_offer = 75000
expected_salary = 70000
print("Is the offer better than expected?", salary_offer > expected_salary)  # True

# 4. Greater than or equal to (>=)
available_seats = 3
required_seats = 3
print("Is there enough seating?", available_seats >= required_seats)  # True

# 5. Equal to (==)
city_entered = "New York"
official_city_name = "New York"
print("Is the entered city correct?", city_entered == official_city_name)  # True

# 6. Password matching (e.g., during login)
entered_password = "DataScience123"
stored_password = "DataScience123"
is_password_correct = entered_password == stored_password
print("Is password correct?", is_password_correct)  # True

# 7. Not equal to (!=)
user_country = "India"
banned_country = "North Korea"
print("Is the user's country allowed?", user_country != banned_country)  # True


# ------------------------------
# Edge Cases / Weird Situations
# ------------------------------

print("\n# Edge cases and weird behavior")

# Comparing int and float
temp_celsius = 25
comfort_temp = 25.0
print("Is temperature exactly comfortable?", temp_celsius == comfort_temp)  # True (int and float compared)

# Comparing string case sensitivity
entered_name = "alice"
correct_name = "Alice"
print("Is the name correct?", entered_name == correct_name)  # False (case matters)

# Comparing different types
print("Is 10 equal to '10'?", 10 == "10")  # False (int vs string)

# Lexicographic string comparison
password1 = "apple"
password2 = "banana"
print("Is 'apple' less than 'banana'?", password1 < password2)  # True (lexicographically)

# Floating point weirdness
a = 0.1 + 0.2
b = 0.3
print("Is 0.1 + 0.2 equal to 0.3?", a == b)  # False due to floating point precision
print("Actual result of 0.1 + 0.2:", a)

# 3. Boolean vs integer comparison
print("True == 1 ?", True == 1)   # True
print("False == 0 ?", False == 0) # True

# None comparison
response = None
print("Was there a response?", response != None)  # False (PEP8 prefers: response is not None)

x = None
print("x == None ?", x == None)           # True (but not recommended)
print("x is None ?", x is None)           # True (recommended way)

# Boolean comparison
is_active = True
is_verified = False
print("Is user active and verified?", is_active == is_verified)  # False

# 6. Empty containers comparison
empty_list = []
empty_dict = {}
print("Is [] == {} ?", empty_list == empty_dict)  # False
