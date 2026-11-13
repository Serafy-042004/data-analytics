bank_balance = 500
savings_goal = 2000
weekly_savings = 200

while bank_balance < savings_goal:

    bank_balance += weekly_savings

    print(f"This week my balance increased to ${bank_balance:,.2f}")

    if bank_balance > savings_goal / 2:
        print(f"Almost there! This week my balance is up to ${bank_balance:,.2f}")

    if bank_balance >= savings_goal * 0.75:
        treat = bank_balance * 0.05
        bank_balance -= treat
        print(f"So close! After treating myself, my balance is up to ${bank_balance:,.2f}")

print(f"Goal met! My current balance is ${bank_balance:,.2f}")
