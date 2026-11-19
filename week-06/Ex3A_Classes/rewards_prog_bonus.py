cust_list = []


class RewardsProgram:

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

    def profile(self):
        print(f"""
            Name: {self.cust_name}
            Phone: {self.phone}
            Email: {self.email}
        """)

    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def add_to_cust_list(self):
        cust_list.append((self.cust_name, self.phone, self.email))


customer1 = RewardsProgram("John Smith", "555-123-4567", "john@email.com")
customer2 = RewardsProgram("Sarah Johnson", "555-987-6543", "sarah@email.com")
customer3 = RewardsProgram("Michael Brown", "555-456-7890", "michael@email.com")


customer1.profile()
customer1.thank_you()
customer1.add_to_cust_list()

customer2.profile()
customer2.thank_you()
customer2.add_to_cust_list()

customer3.profile()
customer3.thank_you()
customer3.add_to_cust_list()


print("\n--- Customer List ---")
print(cust_list)
