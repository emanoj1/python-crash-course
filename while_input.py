# Using a WHILE statement with an Input function
prompt = "Let's talk! If you don't want to, just type 'quit'!"
prompt += "\nSay something:"

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(f"You said: {message.title()}")
    else:
        print("You have quit the session!")

prompt = "Let's talk about cities! If you don't want to, just type 'quit'!"
prompt += "\nName a city:"

# Using TRUE and BREAK
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"\nYour fave city is: {city.title()}")