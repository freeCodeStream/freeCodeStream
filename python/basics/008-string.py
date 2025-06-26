# Strings
# A string is just text inside quotes
greeting = "Hello"
print(greeting)

# You can use single quotes inside double quotes, or escape characters
message = "She said, 'I love Python!'"
print(message)

quote = 'He replied, "Me too!"'
print(quote)

# Quotes inside quotes
# Store your name or city in a variable
name = "Ali"
city = "Amsterdam"
print("My name is", name)
print("I live in", city)

# Multiline String
# A multiline message, like an email
email = """Hello Team,

Please attend the meeting tomorrow at 10:00 AM.

Thanks,
Manager"""
print(email)

# Strings as Arrays (Indexing)
# Get a letter of a name
name = "Fatima"
print(name[0])   # F
print(name[1])   # a

# Looping Through a String
# Loop through a password to hide characters
password = "secret123"
for char in password:
    print("*", end="")  # Prints *********
print()

# String Length
# Count how long a message is
message = "Good morning!"
print("Message length:", len(message))  # 13

# Check String (in)
# Check if someone mentioned "coffee" in a message
text = "Let's go for coffee at 4"
print("coffee" in text)  # True

# Check If Not in
# Check if "tea" is NOT in the message
print("tea" not in text)  # True

# String Slicing
# Show only the first name from a full name
full_name = "Zahra Hussaini"
first_name = full_name[0:5]
print("First name:", first_name)  # Zahra

# Modify String (Uppercase, Lowercase, Title and replace.)
note = "Today is a sunny day."
print(note.upper())     # TODAY IS A SUNNY DAY.
print(note.lower())     # today is a sunny day.
print(note.title())     # Today Is A Sunny Day.
print(note.replace("sunny", "rainy"))  # Today is a rainy day.

# String Concatenation
# Combine first and last name
first = "Omid"
last = "Rahimi"
full = first + " " + last
print("Full name:", full)

# Format Strings
# Insert name and age in a message
name = "Sara"
age = 22
message = f"My name is {name} and I am {age} years old."
print(message)

# Escape Characters
# New lines, tabs, and quotes inside quotes
quote = "She said, \"Python is awesome!\"\nLet's learn it.\tAre you ready?"
print(quote)

# Most Common String Methods
text = "  hello python  "

print(text.strip())     # removes spaces: "hello python"
print(text.upper())     # HELLO PYTHON
print(text.lower())     # hello python
print(text.startswith("  he"))  # True
print(text.endswith("on  "))    # True
print(text.find("python"))      # 8
print(text.count("o"))          # 2
print(text.replace("python", "world"))  # "  hello world  "

# Prefix a string with r to treat backslashes (\) literally,
file_dir = r'C:\python\bin'
print(file_dir)




# String Bad Practices and Their Fixes

# Hardcoding Strings
# BAD: it is not reusable
print("Welcome to Amsterdam!")
print("Welcome to Amsterdam!")

# GOOD:
city = "Amsterdam"
print("Welcome to", city)


# Too Much + for Concatenation
# BAD: It gets messy with conversions.
name = "Ali"
age = 25
print("My name is " + name + " and I am " + str(age) + " years old.")

# GOOD: easy to read
print(f"My name is {name} and I am {age} years old.")


# Not Stripping Input
# BAD: Extra spaces will break the match
user_input = " Ali "
if user_input == "Ali":
    print("Welcome Ali")

# GOOD:
if user_input.strip() == "Ali":
    print("Welcome Ali")


# Wrong Case in Checks
# BAD: It fails if the user types "yes" or "Yes".
command = "Yes"
if command == "YES":
    print("Confirmed")

# GOOD:
if command.strip().lower() == "yes":
    print("Confirmed")


# Magic Strings
# BAD:
user_role = "admin"
if user_role == "admin":
    print("Access granted")

# GOOD:
ROLE_ADMIN = "admin"
if user_role == ROLE_ADMIN:
    print("Access granted")


# Using is for Comparison
# BAD: is checks identity, not value (can cause unexpected bugs).
name = "Fatima"
if name is "Fatima":
    print("Hi Fatima")

# GOOD:
if name == "Fatima":
    print("Hi Fatima")


# Not Using Methods Properly
# BAD: It's not precise — can match notgmail.com
email = "user@gmail.com"
if "@gmail.com" in email:
    print("Gmail user")

# GOOD:
if email.endswith("@gmail.com"):
    print("Gmail user")


# Too Many Escape Characters
# BAD: It’s harder to read and maintain.
msg = "Dear Ali,\n\nThank you.\n\nRegards,\nManager"
print(msg)

# GOOD:
msg = """Dear Ali,

Thank you.

Regards,
Manager"""
print(msg)


# Overusing Replace
# BAD: Becomes unreadable with many replaces.
text = "He is GOOD and SMART"
text = text.replace("GOOD", "kind").replace("SMART", "intelligent")
print(text)

# GOOD:
text = "He is GOOD and SMART"
replacements = {"GOOD": "kind", "SMART": "intelligent"}
for old, new in replacements.items():
    text = text.replace(old, new)
print(text)
