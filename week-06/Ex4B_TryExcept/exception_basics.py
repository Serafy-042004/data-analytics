# 1. ValueError
print("Example 1: ValueError")

try:
    number = int("hello")

except ValueError:
    print("ValueError: Cannot convert text into an integer.")

else:
    print("The number is:", number)

finally:
    print("Let's try another one.\n")


# 2. NameError
print("Example 2: NameError")

try:
    print(customer_name)

except NameError:
    print("NameError: This variable has not been defined.")

else:
    print("Customer name:", customer_name)

finally:
    print("Let's try another one.\n")


# 3. TypeError
print("Example 3: TypeError")

try:
    result = "Hello" + 25

except TypeError:
    print("TypeError: Cannot add a string and an integer.")

else:
    print("Result:", result)

finally:
    print("Let's try another one.\n")


# 4. SyntaxError
print("Example 4: SyntaxError")

try:
    compile("if True print('Hello')", "<string>", "exec")

except SyntaxError:
    print("SyntaxError: The Python code has incorrect syntax.")

else:
    print("The code compiled successfully.")

finally:
    print("Let's try another one.\n")
