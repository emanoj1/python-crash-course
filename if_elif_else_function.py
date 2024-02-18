#Admission price per age group
your_age = 12

if your_age < 4:
    print("Your admission cost is $0!")
elif your_age < 18:
    print("Your admisison cost is $25")
else:
    print("Your admission cost is $40")

#The above can be simplified as follows:
if your_age < 4:
    price = 0
elif your_age < 18:
    price = 25
else:
    price = 40
    
print(f"Your admission cost is ${price}")

#The above can be changed by omitting the ELSE:
if your_age < 4:
    price = 0
elif your_age < 18:
    price = 25
elif your_age <65:
    price = 40
elif your_age >=65:
    price = 20
    
print(f"Your admission cost is ${price}")