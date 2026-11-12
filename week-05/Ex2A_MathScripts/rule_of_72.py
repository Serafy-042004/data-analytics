# Define known values
current_savings = 1000.00
interest_rate = 0.06

# Calculate years to double savings (Rule of 72)
years = 72 / (interest_rate * 100)

# Calculate doubled savings
doubled_balance = current_savings * 2

# Display the results
print(f"Your current savings is ${current_savings:.2f}.")
print(f"At a {interest_rate:.0%} interest rate, your savings account will be worth ${format(doubled_balance, '.2f')} in {format(years, '.1f')} years.")
