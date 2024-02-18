for value in range(6):
   print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

square_numbers = []
for value in range(1,11):
    square_numbers.append(value ** 2)

# print(square_numbers)
square_numbers = [value ** 2 for value in range(1,11)]
print(square_numbers)

#Print numbers 1-20
for numbers in range(1,21,2):
   print(numbers)

#Multiples of 3
three_multiples = []
for number in range(1, 31):
    number = number *3
    three_multiples.append(number)

print(three_multiples)

#Cubed numbers
cubed_number = []
for number in range(1,11):
    number = number ** 3
    cubed_number.append(number)

print(cubed_number)