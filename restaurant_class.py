class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("WELCOME!!")
        print(f"Our {self.restaurant_name.title()} offers {self.cuisine_type.title()} meals.")

    def open_restaurant(self):
        print("We are open 6 PM - 10 PM.")
        print("We are now open! Please come in.")

restaurant = Restaurant('Save Cows Cafe', 'Vegetarian/Vegan')
restaurant.describe_restaurant()
restaurant.open_restaurant()