#A list in a dictionary, page 108

#Store info about the ordered pizza
pizza = {
    'crust': 'thick',
    'toppings': ['cheese, eggplant, paneer']
}

#Summarise the order
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")