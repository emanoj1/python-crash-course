unconfirmed_users = ['alice', 'john', 'manoj']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

for confirmed_user in confirmed_users:    
    print(f"Now Verified: {confirmed_user.title()}")
