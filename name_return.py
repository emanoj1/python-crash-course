'''def formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = formatted_name('john', 'singer', 'doe')
print(f"The name of the singer is {musician}")'''

def formatted_name (first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return(full_name.title())

while True:
    print("\nI am going to ask your name.")
    print("Enter 'q' anytime to quit")

    f_name = input("\n\tWhat is your first name? ")
    if f_name == 'q':
        break

    l_name = input("\tWhat is your last name? ")
    if l_name == 'q':
        break

    the_full_name = formatted_name(f_name, l_name)
    print(f"\nYour full name is {the_full_name}!") 