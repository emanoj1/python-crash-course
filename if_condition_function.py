# Convert bmw to BMW
car_names = ['audi','toyota','lexus','ferrari','dina','porche','bmw','daf','dmc']

for car in car_names:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


# The operator for inequality is !=
toppings = 'mushroom'
if toppings != 'pineapple':
    print("I asked for pineapple on my pizza!")