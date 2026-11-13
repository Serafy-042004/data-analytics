
pay_rate = 17.30
hours_worked = 45

if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = hours_worked * pay_rate

filing_status = input("Enter filing status (single or joint): ").lower()

annual_income = gross_pay * 52

if filing_status == "single":
    if annual_income < 12000:
        tax_rate = 0.05
    elif annual_income < 25000:
        tax_rate = 0.10
    elif annual_income < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

elif filing_status == "joint":
    if annual_income < 12000:
        tax_rate = 0.00
    elif annual_income < 25000:
        tax_rate = 0.06
    elif annual_income < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

else:
    tax_rate = None
    print("Invalid filing status.")

if tax_rate is not None:
    tax_withheld = gross_pay * tax_rate
    net_pay = gross_pay - tax_withheld

    print(f"\nYou worked {hours_worked} hours this period.")
    print(f"Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is ${gross_pay:.2f}")
    print(f"Your filing status is {filing_status}")
    print(f"Your tax withholding for the week is ${tax_withheld:.2f}")
    print(f"Your net pay is ${net_pay:.2f}")
