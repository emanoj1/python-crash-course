#How to copy over a list using the Slice function
my_fave_foods = ['greek salad','indian thali','mix veggetable curry','sandwiches']
friends_fave_food = my_fave_foods[:]

print("\nMy favourite foods:")
print(my_fave_foods)

print("\nMy friends favourite foods:")
print(friends_fave_food)

my_fave_foods.append('Paneer')
print("\nAdding one more to my favourite foods list:")
print(my_fave_foods)