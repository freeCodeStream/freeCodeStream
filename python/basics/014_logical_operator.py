# ---------------------------------------
# Basic Logical Operators: and, or, not
# ---------------------------------------


# === AND Operator Truth Table ===
# Condition A | Condition B | A and B
# ----------- | ----------- | --------
#   True      |   True      |  True   |
#   True      |   False     |  False  |
#   False     |   True      |  False  |
#   False     |   False     |  False  |


# === OR Operator Truth Table ===
# Condition A | Condition B | A or B
# ----------- | ----------- | -------
#   True      |   True      |  True   |
#   True      |   False     |  True   |
#   False     |   True      |  True   |
#   False     |   False     |  False  |


# === NOT Operator Truth Table ===
# Condition | not Condition
# --------- | -------------
#   True    | False
#   False   | True


print("\n=== Real-life Examples ===")

is_weekend = True
has_free_time = False
wants_to_learn = True

# Example 1: Attend Python class only if it's weekend AND you have free time
can_attend_class = is_weekend and has_free_time
print(f"Can attend class (weekend AND free time): {can_attend_class}") # output False

# Example 2: Watch recorded session if you want to learn OR you have free time
can_watch_recording = wants_to_learn or has_free_time
print(f"Can watch recorded session (want to learn OR free time): {can_watch_recording}") # output True

# Example 3: Not having free time
print(f"Do not have free time: {not has_free_time}") # output True

# ---------------------------------------
# 3. Precedence of Logical Operators
# ---------------------------------------

print("\n=== Operator Precedence ===")
print("Precedence Order: NOT > AND > OR")

# Example 1: not has_free_time or is_weekend and wants_to_learn
# From highest to lowest: 1st: not, 2nd: and, 3rd: or
# Why?
#   not has the highest precedence → not has_free_time is evaluated first.
#   Then and → is_weekend and wants_to_learn
#   Finally or combines the two sub-results.
# Equivalent: (not has_free_time) or (is_weekend and wants_to_learn)

result = not has_free_time or is_weekend and wants_to_learn
print(f"Result of 'not has_free_time or is_weekend and wants_to_learn': {result}") # output True

# Example 2: Parentheses can change outcome
# evaluated order would be as below
# Parentheses first → (has_free_time or is_weekend)
# Then not → not (result of step 1)
# Then and → (result of step 2) and wants_to_learn
# Because of the parentheses, the or happens first, then not, then and.
result_with_parentheses = not (has_free_time or is_weekend) and wants_to_learn
print(f"Result of 'not (has_free_time or is_weekend) and wants_to_learn': {result_with_parentheses}") # output False

# ---------------------------------------
# 4. Multiple Operators with Same Precedence
# ---------------------------------------

print("\n=== Same Precedence: Evaluation Left to Right ===")

# Example: a and b and c
a = True
b = False
c = True
result = a and b and c  # Evaluated as ((a and b) and c)
print(f"Result of 'a and b and c' (True, False, True): {result}") # output False

# Example: a or b or c
result = a or b or c  # Evaluated as ((a or b) or c)
print(f"Result of 'a or b or c' (True, False, True): {result}") # output True

# ---------------------------------------
# 5. Weird Cases
# ---------------------------------------

print("\n=== Weird Cases ===")

# Case 1: Logical operators with non-boolean values
# Empty strings "", 0, None, empty lists [], empty dictionaries {}, etc., are falsy.
# "or" returns the first truthy value or the last value if none are truthy.
username = ""
is_authenticated = username or "Guest"
print(f"Username is set to: {is_authenticated}")  # "Guest" because "" is falsy

# Case 2: 'and' stops at the first falsy value and returns it.
# If all values are truthy, and returns the last value.
print(f"Result of '5 and 0': {5 and 0}")         # 0
print(f"Result of '5 and 10': {5 and 10}")       # 10

# Case 3: 'or' returns the first truthy value
print(f"Result of '0 or 10': {0 or 10}")         # 10
print(f"Result of '0 or False or [] or \"Hello\"': {0 or False or [] or 'Hello'}")  # 'Hello'

# Case 4: Mixing with arithmetic (not recommended)
score = 0
bonus = 10
final_score = score and bonus  # 0, because score is falsy
print(f"Final score using 'and': {final_score}")

# Safer alternative
final_score = bonus if score > 0 else score
print(f"Final score using conditional: {final_score}")
