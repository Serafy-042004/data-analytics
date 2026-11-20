
class Restaurant:

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        self.number_served += 1

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")

    def customer_rating(self):
        rating = int(input(
            "How would you rate your experience today "
            "on a scale of 1-5 (5 being excellent)? "
        ))

        if 1 <= rating <= 5:
            self.customer_ratings.append(rating)

            average = sum(self.customer_ratings) / len(self.customer_ratings)

            print(
                f"Your rating was {rating}. "
                f"The average rating for this restaurant is {average:.2f}"
            )

        else:
            print("Invalid rating. Please enter a number between 1 and 5.")


restaurant1 = Restaurant("Wendy's", "Burgers")
restaurant2 = Restaurant("Taco Bell", "Mexican food")
restaurant3 = Restaurant("Dunkin' Donuts", "Donuts and coffee")

restaurant1.describe_rest()
restaurant1.rest_open()

restaurant2.describe_rest()
restaurant2.rest_open()

restaurant3.describe_rest()
restaurant3.rest_open()

restaurant1.add_num_served()
restaurant1.add_num_served()
restaurant2.add_num_served()
restaurant3.add_num_served()

restaurant1.print_num_served()
restaurant2.print_num_served()
restaurant3.print_num_served()

restaurant1.customer_rating()
restaurant1.customer_rating()

restaurant2.customer_rating()
restaurant2.customer_rating()

restaurant3.customer_rating()
restaurant3.customer_rating()
