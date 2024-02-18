# USING MULTIPLE LISTS WITH IF
available_toppings = ['tomato slices','green olives','black olives','pineapple','paneer','capsicum','soya','feta cheese']

requested_toppings = ['tomato slices','green olives','black olives','french fries']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"{requested_topping.title()} are on your pizza.")
    else:
        print(f"Sorry! {requested_topping.title()} is not in our available toppings.")

print("\nYour pizza is now ready for the oven!")

#ANSWER
#Tomato Slices are on your pizza.
#Green Olives are on your pizza.
#Black Olives are on your pizza.
#Sorry! French Fries is not in our available toppings.

#Your pizza is now ready for the oven!