# Is the user an adult?
age = 20
is_adult = age >= 18
print("Is the user an adult?", is_adult)  # True

# Is the email field empty?
email_input = ""
is_email_provided = bool(email_input)
print("Has the user provided an email?", is_email_provided)  # False

# Is the shopping cart empty?
shopping_cart = []
is_cart_empty = not bool(shopping_cart)
print("Is the shopping cart empty?", is_cart_empty)  # True

# Did the user accept the terms?
user_response = "yes"
did_accept_terms = user_response.lower() == "yes"
print("Did the user accept the terms?", did_accept_terms)  # True

# Is the temperature too cold?
temperature_celsius = 10
is_too_cold = temperature_celsius < 15
print("Is the temperature too cold?", is_too_cold)  # True

# Is the password strong?
password = "secure123"
is_password_strong = len(password) >= 8
print("Is the password strong?", is_password_strong)  # True

# ---------- Falsy Values in Python ----------

# These values all evaluate to False when converted to bool()

falsy_values = [
    False,      # Boolean false itself
    None,       # Null value
    0,          # Integer zero
    0.0,        # Float zero
    0j,         # Complex number with 0 real and imaginary parts
    "",         # Empty string
    [],         # Empty list
    {},         # Empty dictionary
    set(),      # Empty set
    tuple(),    # Empty tuple
    range(0)    # Empty range
]

print("\n--- Falsy Values Examples ---")
for index, value in enumerate(falsy_values):
    print(f"Example {index + 1}: {value!r} is falsy?", bool(value))  # All should print False
