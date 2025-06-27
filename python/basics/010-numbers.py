import random

# ---------------------------
# 1. Integers and Floats
# ---------------------------

# A person's age (integer)
age_in_years = 28

# The price of a coffee in dollars (float)
coffee_price_usd = 4.75

# Body temperature in Celsius (float)
body_temperature_celsius = 36.6

print("=== Integers and Floats ===")
print(f"Age: {age_in_years} years")
print(f"Coffee Price: ${coffee_price_usd}")
print(f"Body Temperature: {body_temperature_celsius} °C")
print()

# ---------------------------
# 2. Underscores in Numbers
# ---------------------------

# National debt in dollars (large number for readability)
national_debt_euro_2024 = 491_600_000_000

# Distance from Earth to Mars in kilometers (average)
earth_to_mars_km = 225_000_000

print("=== Underscores in Numbers ===")
print(f"US National Debt: €{national_debt_euro_2024:,}")
print(f"Average Distance to Mars: {earth_to_mars_km:,} km")
print()

# ---------------------------
# 3. Random Number Examples
# ---------------------------

# Simulate drawing a lottery number between 1 and 49
lottery_number = random.randint(1, 49)

# Generate a random discount between 5% and 25%
random_discount_percent = round(random.uniform(5.0, 25.0), 2)

print("=== Random Numbers ===")
print(f"Today's Lucky Lottery Number: {lottery_number}")
print(f"Random Discount: {random_discount_percent}% off")
print()

# ---------------------------
# 4. Complex Numbers (Bonus)
# ---------------------------

# Used in electrical engineering to represent impedance
impedance = 7 + 2j

print("=== Complex Numbers ===")
print(f"Electrical Impedance: {impedance}")
print(f"Impedance Magnitude: {abs(impedance)}")
print()

# ---------------------------
# 5. Rare but Useful Type Conversions
# ---------------------------

# Convert a string representing height to float
height_input = "180.5"
height_cm = float(height_input)
print(f"Height from string to float: {height_cm} cm")

# Convert a boolean to integer (True = 1, False = 0)
is_member = False
member_points = int(is_member)
print(f"Membership Status (bool to int): {member_points}")

# Convert a float to a complex number
gold_price = 1932.75
gold_price_complex = complex(gold_price)
print(f"Gold Price as Complex: {gold_price_complex}")

# Convert an integer to binary, octal, and hexadecimal strings
daily_steps = 1023
steps_binary = bin(daily_steps)
print(f"Daily Steps in Binary: {steps_binary}")

steps_octal = oct(daily_steps)
print(f"Daily Steps in Octal: {steps_octal}")

steps_hex = hex(daily_steps)
print(f"Daily Steps in Hex: {steps_hex}")
