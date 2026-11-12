# Import math module
import math

# Ask for room dimensions
length = float(input("Enter room length in feet: "))
width = float(input("Enter room width in feet: "))

# Calculate room area
area = length * width

# Calculate tiles needed, including 10% extra
tiles_needed = math.ceil(area * 1.10)

# Calculate full boxes needed
boxes_needed = math.ceil(tiles_needed / 12)

# Calculate total tiles purchased
total_tiles = boxes_needed * 12

# Display results
print(f"Room area: {area:.2f} square feet")
print(f"Tiles needed with extra: {tiles_needed}")
print(f"Boxes to purchase: {boxes_needed}")
print(f"Total tiles purchased: {total_tiles}")
