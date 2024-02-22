#A list in a Dictionary

# Write a code to print back what pizza crust and toppings were ordered

#Store info about the pizza
pizza  = {
    'crust': 'thick',
    'toppings': ['green peppers', 'green olives', 'bitey cheddar cheese', 'paneer', 'potato slices']
}
#print the ordered pizza crust
print(f"You ordered a {pizza['crust']}-crust pizza with these toppings:")

#print the toppings one by one
for topping in pizza['toppings']:
    print(topping.title())