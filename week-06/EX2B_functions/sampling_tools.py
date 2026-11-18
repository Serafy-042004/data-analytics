
import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
            'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp',
            'Surge Protector']

print("Original Product List:", products)

product_of_day = random.choice(products)
print("\nProduct of the Day:", product_of_day)

survey_products = random.sample(products, 3)
print("\nProducts Selected for Survey:", survey_products)

random.shuffle(products)
print("\nRandomized Product List:", products)

daily_transactions = random.randint(50, 300)
print("\nDaily Transaction Count:", daily_transactions)
