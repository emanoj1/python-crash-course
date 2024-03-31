#Pass a list into a Function

def users_greeting(names):
    for name in names:
        message = f"Hello {name.title()}!"
        print(message)

usernames = ['manoj', 'hanna', 'john']
users_greeting(usernames)

