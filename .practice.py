'''def make_pizza(*toppings):
    print("\nYour pizza toppings are:")
    for topping in toppings:
        print(f"\t- {topping}")

make_pizza('pepper', 'tomatoes', 'paneer', 'potato slices', 'satay powder')'''

def sandwich(*items):
    print("\nYour sandwich has the following items in it:")
    for item in items:
        print(f"\t - {item}")

sandwich('cheddar cheese', 'tomato', 'cucumber', 'olives', 'mustard sauce', 'lettuce')