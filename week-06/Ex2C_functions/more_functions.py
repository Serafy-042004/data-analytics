def display_mailing_label(name, address, city, state, zip):
    print(name)
    print(address)
    print(f"{city}, {state} {zip}")



display_mailing_label("John Smith", "123 Main Street", "Los Angeles", "CA", "90001")

print("\n")

display_mailing_label("Sarah Johnson", "456 Oak Avenue", "San Diego", "CA", "92101")


print("\n")

def add_numbers(*args):
    result = sum(args)
    numbers = " + ".join(str(num) for num in args)
    print(f"{numbers} = {result}")



add_numbers(10)

add_numbers(10, 20)

add_numbers(10, 20, 30, 40, 50)


print("\n")


def display_receipt(total_due, amount_paid):

    difference = amount_paid - total_due

    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")

    if difference > 0:
        print(f"Change Due: ${difference:.2f}")

    elif difference == 0:
        print("Change Due: $0.00")

    else:
        print(f"Remaining Balance: ${abs(difference):.2f}")


display_receipt(25.00, 30.00)

print("\n")

display_receipt(25.00, 25.00)

print("\n")

display_receipt(25.00, 20.00)
