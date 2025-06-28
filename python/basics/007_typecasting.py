LINE_BREAKER = "\n********************\n"
print("Typecasting Demonstration")

print("String to Integer")
age_input = input("Enter your age: ")
print("\nBefore casting:")
print("Value:", age_input, "| Type:", type(age_input))

age = int(age_input)
print("\nAfter casting to int:")
print("Value:", age, "| Type:", type(age))

print(LINE_BREAKER)

print("String to Float")
salary_input = input("\nEnter your monthly salary (in decimal): ")
print("\nBefore casting:")
print("Value:", salary_input, "| Type:", type(salary_input))

monthly_salary = float(salary_input)
print("After casting to float:")
print("Value:", monthly_salary, "| Type:", type(monthly_salary))

print(LINE_BREAKER)

print("Float to Integer (cutting decimal part)")
height_in_feet = float(input("\nEnter your height in cm (e.g., 178.7): "))
print("\nBefore casting:")
print("Value:", height_in_feet, "| Type:", type(height_in_feet))

height_in_feet_int = int(height_in_feet)
print("After casting to int:")
print("Value:", height_in_feet_int, "| Type:", type(height_in_feet_int))

print(LINE_BREAKER)

print("Integer to Float")
num_of_books = int(input("\nEnter the number of books you read last year: "))
print("\nBefore casting:")
print("Value:", num_of_books, "| Type:", type(num_of_books))

books_as_float = float(num_of_books)
print("After casting to float:")
print("Value:", books_as_float, "| Type:", type(books_as_float))

print(LINE_BREAKER)

print("Integer to String")
zipcode = int(input("\nEnter your ZIP code: "))
print("\nBefore casting:")
print("Value:", zipcode, "| Type:", type(zipcode))

zipcode_str = str(zipcode)
print("After casting to string:")
print("Value:", zipcode_str, "| Type:", type(zipcode_str))

print(LINE_BREAKER)

# If you want to treat 'yes' as True and 'no' as False, you have to convert them manually:
print("String to Boolean")
has_pet_input = input("\nDo you have a pet? (yes/no): ")
print("\nBefore casting:")
print("Value:", has_pet_input, "| Type:", type(has_pet_input))

has_pet_bool = bool(has_pet_input.lower() == "yes")
print("After casting to boolean:")
print("Value:", has_pet_bool, "| Type:", type(has_pet_bool))

has_pet_bool = bool(has_pet_input.lower() == "no")
print("After casting to boolean:")
print("Value:", has_pet_bool, "| Type:", type(has_pet_bool))

print(LINE_BREAKER)

print("List to Tuple")
favorite_fruits = input("\nEnter your favorite fruits separated by commas: ").split(', ')
print("\nBefore casting:")
print("Value:", favorite_fruits, "| Type:", type(favorite_fruits))

favorite_fruits_tuple = tuple(favorite_fruits)
print("After casting to tuple:")
print("Value:", favorite_fruits_tuple, "| Type:", type(favorite_fruits_tuple))

print(LINE_BREAKER)

print("Tuple to List")
address_tuple = ("123", "Maple Street", "New York")
print("\nOriginal tuple (simulated address):", address_tuple, "| Type:", type(address_tuple))

address_list = list(address_tuple)
print("After casting to list:")
print("Value:", address_list, "| Type:", type(address_list))

print(LINE_BREAKER)

print("String to List (e.g., username to characters)")
username = input("\nEnter your username: ")
print("\nBefore casting:")
print("Value:", username, "| Type:", type(username))

username_chars = list(username)
print("After casting to list of characters:")
print("Value:", username_chars, "| Type:", type(username_chars))
