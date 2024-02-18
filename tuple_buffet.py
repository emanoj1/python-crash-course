#Challenge exercise 4-13 Buffet

#ORIGINAL food items
buffet_list = ('french fries','fried cauliflower','pasta','mixed veg curry','milk shake')
print("Our buffet only has the following food tiday:")
for buffet_item in buffet_list:
    print(buffet_item.title())

#MODIFIED food items

new_buffet_list = ('french fries','fried potatoes','pasta','rich tomato gravy','milk shake')
print("\nWe have a new buffet list. Ignore the last one!")
for new_food_item in new_buffet_list:
    print(new_food_item.title())

# ANSWER
# Our buffet only has the following food tiday:
# French Fries
# Fried Cauliflower
# Pasta
# Mixed Veg Curry
# Milk Shake

# We have a new buffet list. Ignore the last one!
# French Fries
# Fried Potatoes
# Pasta
# Rich Tomato Gravy
# Milk Shake