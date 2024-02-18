# 5-10) Username check from a list

current_users = ['jade123','emma56','admin','emanoj','kite59']
new_users = ['brian_purple','emma56','hastilyme','peekaboo123','KITE59']

current_users_lowercase = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lowercase:
        print(f"Sorry! {new_user} is NOT available")
    else:
        print(f"Great! {new_user} is available!")
