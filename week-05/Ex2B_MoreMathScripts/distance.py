# Import math module
import math

# Ask for coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Display result
print(f"The distance between the coordinates is {distance:.2f}")
