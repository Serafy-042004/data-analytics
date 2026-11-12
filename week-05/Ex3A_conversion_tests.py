# Description: This script tests various numeric
# conversion techniques
# Author: Henry

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# Test converting variables to integers
# print(int(a))  # ValueError: cannot convert decimal string to integer
b_int = int(b)
# print(int(c))  # ValueError: contains letters
# print(int(d))  # ValueError: contains letters


# Test converting variables to floats
a_float = float(a)
b_float = float(b)
# print(float(c))  # ValueError: contains letters
# print(float(d))  # ValueError: contains letters


# Convert variable a to float, then integer
a_int = int(float(a))


# Use slicing to extract numeric portions
a_slice = float(a.strip()[0:5])
b_slice = int(b[0:2])
c_slice = int(c[0:3])
d_slice = int(d[7:8])


# Remove leading and trailing spaces using strip()
print("Variable a without spaces:", a.strip())
print("Variable d without spaces:", d.strip())


# Display original variables and their types
print("\n--- Original Variables ---")
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))


# Display integer and float conversions
print("\n--- Type Conversions ---")
print(a_float, type(a_float))
print(a_int, type(a_int))
print(b_int, type(b_int))
print(b_float, type(b_float))


# Display sliced variables and their types
print("\n--- Slicing Results ---")
print(a_slice, type(a_slice))
print(b_slice, type(b_slice))
print(c_slice, type(c_slice))
print(d_slice, type(d_slice))