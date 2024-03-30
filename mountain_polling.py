# Take inputs of fave mountains to climb from a user and display the results at the end

# SOLUTION 1 (remove the "#" comment-out to test)
#next_poll = 'y'
#while next_poll == 'y':
#    your_name = input("What is your name: ")
#    mountain_name = input("What mountain do you want to climb: ")
#    print(f"{your_name.title()} would like to climb Mt.{mountain_name.title()}!")
#    next_poll = input("\nDo you want another person to poll (y/n) :")

# SOLUTION 2
responses = {}

polling_status = True

while polling_status:
    entrant_name = input("Your name: ")
    entrant_answer = input("Your mountain: ")

    responses[entrant_name] = entrant_answer

    next_entrant = input("Another user participation (y/n)?")

    if next_entrant == 'n':
        polling_status = False

print("\n----RESULTS----")

for entrant_name, entrant_answer in responses.items():
    print(f"{entrant_name.title()} wants to climb Mt.{entrant_answer.title()}")