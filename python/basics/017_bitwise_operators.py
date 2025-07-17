"""
Bitwise operators let you manipulate individual bits of numbers.
Think of them like switches (1 = on, 0 = off) – bitwise operations
let you turn these switches on/off or compare them, which can be
super handy in low-level programming, device control, optimization,
etc.

"""

"""
Bitwise Operators Table
"   &   (AND)":          "Returns 1 if both bits are 1",
"   |   (OR)":           "Returns 1 if at least one bit is 1",
"   ^   (XOR)":          "Returns 1 if bits are different",
"   ~   (NOT)":          "Inverts the bits (1 -> 0, 0 -> 1)",
"   <<  (Left Shift)":   "Shifts bits to the left (multiply by 2)",
"   >>  (Right Shift)":  "Shifts bits to the right (divide by 2)"
"""

# Bitwise AND (&) - checks if both bits are 1
room_status = 0b011  # Binary: 011 means Heater=1, AC=1
HEATER_MASK = 0b001
AC_MASK = 0b010

has_heater = room_status & HEATER_MASK
has_ac = room_status & AC_MASK

print("Heater status (0 = OFF, not 0 = ON):", has_heater)
print("AC status (0 = OFF, not 0 = ON):", has_ac)

# Bitwise OR (|) - combine features
turn_on_both = HEATER_MASK | AC_MASK
print("Turn ON heater and AC together:", bin(turn_on_both))

# Bitwise XOR (^) - toggle feature
alarm_status = 1  # alarm is ON
TOGGLE_MASK = 1
alarm_status ^= TOGGLE_MASK
print("Alarm status after toggle (0 = OFF, 1 = ON):", alarm_status)

# Bitwise NOT (~) - flip all bits
permissions = 0b00001111
flipped = ~permissions
print("Permissions before:", bin(permissions))
print("Permissions flipped:", bin(flipped))

# Bitwise Left Shift (<<) - multiply by 2
base_storage = 4
print("Double storage:", base_storage << 1, "GB")

# Bitwise Right Shift (>>) - divide by 2
bandwidth = 100
print("Half bandwidth:", bandwidth >> 1, "Mbps")

# --- Edge Cases ---

x = 0
print("~0 =", ~x)

# Even or odd check using bitwise AND
num = 29
print("Number:", num)
print("Check last bit with & 1:", num & 1)  # 1 means odd, 0 means even

# Large shift
print("1 << 100 =", 1 << 100)

# Negative right shift
negative = -8
print("-8 >> 2 =", negative >> 2)

# XOR swap (no temporary variable)
a = 5
b = 3
a ^= b
b ^= a
a ^= b
print("Swapped values: a =", a, ", b =", b)

# more simple example
x = 12  # binary: 1100
y = 5   # binary: 0101

print("x & y =", x & y)
print("x | y =", x | y)
print("x ^ y =", x ^ y)
print("~x =", ~x)
print("x << 1 =", x << 1)
print("x >> 1 =", x >> 1)
