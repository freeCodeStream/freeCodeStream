# Whitespace and indentation

# Python uses whitespace and indentation to construct the code structure.
# indentation in your code is used to format the code.

# advantages
# 1. you’ll never miss a block’s beginning or ending code, unlike in other programming languages, such as Java or C#.
# 2. the coding style is essentially uniform. by looking to another developer’s code, that code looks the same as yours.
# 3. the code is more readable and clearer than other programming languages.

# Comments
# The comments are as important as the code because they describe why a piece of code was written.
# When the Python interpreter executes the code, it ignores the comments.
# In Python, a single-line comment begins with a hash (#) symbol followed by the comment. For example:

# This is a single line comment in Python


# Continuation of statements
# Python uses a newline character to separate statements. It places each statement on one line.
# However, a long statement can span multiple lines by using the backslash (\) character.
a = "True"
b = "False"
c = "True"
if (a == True) and (b == False) and \
   (c == True):
    print("Continuation of statements")

# Identifiers:
# Identifiers are names that identify variables, functions, modules, classes, and other objects in Python.
# The name of an identifier needs to begin with a letter or underscore (_). The rest can be alphanumeric or underscore.
# # Python identifiers are case-sensitive. For example, the counter and Counter are different identifiers.
# In addition, you cannot use Python keywords for naming identifiers.

# Keywords
# Some words have special meanings in Python. They are called keywords.
# Python is a growing and evolving language. So its keywords will keep increasing and changing.
# but don't worry, you can check it with following python code
import keyword
print(keyword.kwlist)

# String literals
# Python uses single quotes ('), double quotes ("), triple single quotes (''') and triple-double quotes (""") to denote
# a string literal. The string literal needs to be surrounded with the same type of quotes.
# For example, if you use a single quote to start a string literal, you need to use the same single quote to end it.

s = 'This is a string'
print(s)
s = "Another string using double quotes"
print(s)
s = ''' string can span
        multiple line '''
print(s)