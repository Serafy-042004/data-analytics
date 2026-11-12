# Import math module
import math

# Ask for number of tourists
people = int(input("How many tourists are going on the tour? "))

# Define van rental cost
van_cost = 250
seats_per_van = 15

# Calculate number of vans needed
vans_needed = math.ceil(people / seats_per_van)

# Calculate total rental cost
total_cost = vans_needed * van_cost

# Calculate cost per person
cost_per_person = total_cost / people

# Display results
print(f"Number of tourists: {people}")
print(f"Vans needed: {vans_needed}")
print(f"Total van rental cost: ${total_cost:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")
#Money to charge 19.74, 750.12, 3 vans, becuase decimal values.