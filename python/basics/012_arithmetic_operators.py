# In Python programming, Operators in general are used to perform operations on values and variables.
# These are standard symbols used for logical and arithmetic operations.
# In this article, we will look into arithmetic Python operators.

# OPERATORS: These are the special symbols. Eg- + , * , /, etc.
# OPERAND: It is the value on which the operator is applied.
# Types of Operators in Python
# Arithmetic Operators
    #   +       addition
    #   -       subtraction
    #   *       Multiplication
    #   /       Division (float)
    #   //      Division (floor)
    #   %       Modulus
    #   **      Power

# Addition (+)
# Example: Calculating total cost of groceries
price_apple = 1.20
price_banana = 0.50
total_cost = price_apple + price_banana
print("Total cost of apple and banana:", total_cost)

# Subtraction (-)
# Example: Calculating remaining balance after a purchase
wallet_balance = 50.00
item_cost = 35.75
remaining_balance = wallet_balance - item_cost
print("Remaining wallet balance:", remaining_balance)

# Multiplication (*)
# Example: Total cost for multiple items
coffee_price = 3.50
quantity = 4
total_coffee_cost = coffee_price * quantity
print("Total cost for 4 coffees:", total_coffee_cost)

# Division (/)
# Example: Splitting a bill among friends
total_bill = 120.00
num_friends = 3
share_per_friend = total_bill / num_friends
print("Each friend pays:", share_per_friend)

# Modulus (%)
# Example: Finding out leftover slices of pizza
total_slices = 17
slices_per_person = 5
leftover_slices = total_slices % slices_per_person
print("Leftover pizza slices:", leftover_slices)

# Exponentiation (**)
# Example: Compound interest calculation (simplified)
principal = 1000  # Initial investment
rate = 1.05       # 5% growth per year
years = 3
future_value = principal * (rate ** years)
print("Future value after 3 years:", future_value)

# Floor Division (//)
# Example: Calculating how many full boxes can be packed
total_items = 53
items_per_box = 10
full_boxes = total_items // items_per_box
print("Number of full boxes:", full_boxes)

# Rare case on Negative numbers with floor division
# Good Practice: Be cautious with negative operands
negative_div = -17 // 4
print("Floor division with negative number (-17 // 4):", negative_div)  # Result is -5

# Rare case on Modulo with negative operands
# BAD Practice: Assuming modulo always returns a positive number
mod_result = -17 % 4
print("Modulo with negative number (-17 % 4):", mod_result)  # Result is 3 in Python

# Good practice: Always verify expected behavior with negative operands
# Some other languages (e.g., C/C++) behave differently with negative mod

# BAD Practice Example: Mixing float and int without conversion
# This can cause precision or type issues in financial apps
price = 9.99
quantity = 3
# careless_total = price * quantity + " USD"  # ❌ TypeError
# Good Practice:
formatted_total = f"{price * quantity:.2f} USD"
print("Formatted total cost:", formatted_total)

# BMI (Body Mass Index) Calculation = weight / (height in m)^2
weight_kg = 72
height_cm = 175
height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)
print("Calculated BMI:", round(bmi, 2))

