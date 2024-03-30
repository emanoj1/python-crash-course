# Prompt user to enter a series of pizza toppings until they quit

toppings_prompt = "Name a topping you would like on your pizza: "

while True:
    toppings = input(toppings_prompt)
    if toppings == 'quit':
        break
    else:
        print(f"\nI will add {toppings.title()} on yur pizza.")

