# assignment_operators_examples.py

# Basic Assignment Operator (=)
# Scenario: Assigning values to variables representing a freelancer's earnings
monthly_income = 5000  # Assigns 5000 to monthly_income
monthly_expenses = 3000
savings = monthly_income - monthly_expenses
print("Initial Savings:", savings)

# += operator (Addition Assignment)
# Scenario: Bonus received during the month
monthly_income += 1000  # Equivalent to: monthly_income = monthly_income + 1000
print("Income after bonus:", monthly_income)

# -= operator (Subtraction Assignment)
# Scenario: Unexpected bill
monthly_expenses -= 500  # Equivalent to: monthly_expenses = monthly_expenses - 500
print("Expenses after discount:", monthly_expenses)

# *= operator (Multiplication Assignment)
# Scenario: Overtime pay multiplier
hourly_rate = 50
overtime_hours = 10
hourly_rate *= 1.5  # Overtime rate increased by 50%
overtime_earnings = hourly_rate * overtime_hours
print("Overtime Earnings:", overtime_earnings)

# /= operator (Division Assignment)
# Scenario: Splitting rent with roommates
total_rent = 2400
num_roommates = 3
total_rent /= num_roommates  # Each roommate's share
print("Rent per roommate:", total_rent)

# %= operator (Modulus Assignment)
# Scenario: Leftover cookies after sharing equally
total_cookies = 23
num_friends = 4
leftover_cookies = total_cookies
leftover_cookies %= num_friends  # Modulus gives the leftover
print("Leftover cookies:", leftover_cookies)

# **= operator (Exponentiation Assignment)
# Scenario: Investment doubling every year
investment = 1000
investment_growth_factor = 2  # Doubles every year
investment **= 3  # 3 years of doubling
print("Investment after 3 years:", investment)

# //= operator (Floor Division Assignment)
# Scenario: Number of full boxes you can make with apples
total_apples = 53
apples_per_box = 10
boxes = total_apples
boxes //= apples_per_box
print("Number of full apple boxes:", boxes)

# -------------------------
# Weird Case Scenarios
# -------------------------

# 1. Using += with strings
message = "Data"
message += " Science"
print("Concatenated message:", message)  # Works fine!

# 2. Mixing types can cause issues (like: TypeError)
# price = 100
# price += "50"
# print(f"Unexpected output: {price}")

# 3. Using /= with zero can cause ZeroDivisionError
# amount = 100
# divider = 0
# amount /= divider  # ZeroDivisionError
# print(f"ZeroDivisionError detected {amount}")

# 4. Floating-point floor division weirdness
value = 5.0
value //= 2  # Expect 2, not 2.0
print("Floor division result (float):", value)

# 5. Using assignment operators with lists (mutable types)
grocery_list = ["milk"]
grocery_list += ["bread", "eggs"]
print("Updated grocery list:", grocery_list)

# += with lists modifies in place, but beware:
original_list = [1, 2, 3]
alias_list = original_list
original_list += [4]
print("Original List:", original_list)
print("Alias List:", alias_list)  # Also affected, since both refer to same object

