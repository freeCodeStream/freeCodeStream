# Python Data Types
# Category          Data Type
# Numeric	–	int, float, complex
# Sequence	–	string, list, tuple, range
# Mapping	–	dict
# Boolean	–	bool
# Set		–	set, frozenset
# Binary 	–	bytes, bytearray, memoryview
# None Type:	NoneType


# Numeric types
integer_num = 42  # int
float_num = 3.14  # float
complex_num = 2 + 3j  # complex

print(type(integer_num))  # Output: <class 'int'>
print(type(float_num))    # Output: <class 'float'>
print(type(complex_num))  # Output: <class 'complex'>

# Sequence types
string_var = "Hello, Python!"  # string
list_var = [1, 2, 3, 4, 5]  # list
tuple_var = (10, 20, 30)  # tuple

print(string_var)
print(string_var[0])
print(type(string_var))  # Output: <class 'str'>
print(type(list_var))    # Output: <class 'list'>
print(type(tuple_var))   # Output: <class 'tuple'>

number_as_string = "123" + "456"
print(number_as_string) # python recognize it as string and will concatenate it

# Mapping type
dict_var = {"name": "Alice", "age": 25}  # dict
print(type(dict_var))  # Output: <class 'dict'>

# Boolean type
bool_var = True  # bool
print(type(bool_var))  # Output: <class 'bool'>

# Set types
set_var = {1, 2, 3, 4}  # set
frozenset_var = frozenset([5, 6, 7, 8])  # frozenset

print(type(set_var))  # Output: <class 'set'>
print(type(frozenset_var))  # Output: <class 'frozenset'>

# Binary types
bytes_var = b"Hello"  # bytes
bytearray_var = bytearray(5)  # bytearray
memoryview_var = memoryview(bytes(5))  # memoryview

print(type(bytes_var))  # Output: <class 'bytes'>
print(type(bytearray_var))  # Output: <class 'bytearray'>
print(type(memoryview_var))  # Output: <class 'memoryview'>
