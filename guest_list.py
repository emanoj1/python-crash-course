# Python Crash Course: 3-4 Guest List Challenge

# List of people invited to dinner
guest_list = ['grandma', 'grandad', 'dad', 'sister', 'mother', 'wife', 'uncle']

#Print invitations for each person
print(f"Hey {guest_list[0]}, You are invited for dinner!")
print(f"Hey {guest_list[1]}, You are invited for dinner!",guest_list[0],"is coming too")
print(f"Hey {guest_list[2]}, You are invited for dinner!")
print(f"Hey {guest_list[3]}, You are invited for dinner! Everyone is coming.")
print(f"Hey {guest_list[4]}, You are invited for dinner! Whole family will be there.")
print(f"Hey {guest_list[5]}, You are invited for dinner! Warning - the noisy bunch expected!")
print(f"Hey {guest_list[6]}, You are invited for dinner! You will be happy!")

# 1 guest can't make it. 
print(f"\nSorry! An update. {guest_list[5]} can't make it unfortunately.")

#Replace with another guest
guest_list[5] = 'aunty'

# Print invitations again
print("\nThis is the new updated guest list!\n")
print(f"Hey {guest_list[0]}, You are invited for dinner!")
print(f"Hey {guest_list[1]}, You are invited for dinner!",guest_list[0],"is coming too")
print(f"Hey {guest_list[2]}, You are invited for dinner!")
print(f"Hey {guest_list[3]}, You are invited for dinner! Everyone is coming.")
print(f"Hey {guest_list[4]}, You are invited for dinner! Whole family will be there.")
print(f"Hey {guest_list[5]}, You are invited for dinner! Warning - the noisy bunch expected!")
print(f"Hey {guest_list[6]}, You are invited for dinner! You will be happy!")

# Bigger dinner table found 
print(f"\nMe AGAIN! Another update. I got a large table, so inviting more people!")

# Add new guest to the TOP of the list
guest_list.insert(0, 'great-great grandfather')

# Add new guest to the MIDDLE of the list
guest_list.insert(4, 'great-great grandmother')

# Add new guest to the BOTTOM of the list
guest_list.insert(9, 'great-great uncle')

# Print new invitations for these people
print(f"\nWelcome to the party {guest_list[0]},{guest_list[4]},{guest_list[6]}!")

#Print the full guest list
print(f"\nThis is the full guest list: {', ' .join(guest_list)}!")

# Shrinking guest list announcement
print(f"\nBAD NEWS! We have a change of table, and we can accomodate only 2 people to dine with me. SORRY!")

# Shrinking guest list - popping 1
popped_guest = guest_list.pop()
print(f"\nDear {popped_guest}, you can't join me. Better luck next time!")

# Shrinking guest list - popping 2
popped_guest = guest_list.pop()
print(f"\nDear {popped_guest}, Not this time. Surely, next time!")

# Shrinking guest list - popping 1
popped_guest = guest_list.pop()
print(f"\n Dear {popped_guest}, Don't be angry! The best for you is next time!")