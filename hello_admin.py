# 5-8, 5-9) Greet the Admin from a username list

usernames = ['pjinkett','athomas','emanoj','admin','jack2342']

if usernames == []:
    print("We need to find some users!")
else:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again!")

#Another method for no users check

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again!")
else:
    print("We need to find some users!")