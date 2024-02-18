# Slice an item off the list by specifying the first and last elements you want to work with. If you need only the first 3 retained, give o as first and 3 as last
players = ['michael','emma','john','thomas','eli']
print(players[0:3])
#Answer: ['michael', 'emma', 'john']

# You can write the above command as below to get the same result. It automatically starts at 0.
players = ['michael','emma','john','thomas','eli']
print(players[:3])
#Answer: ['michael', 'emma', 'john']

# The reverse. Retains from the 2nd position.
players = ['michael','emma','john','thomas','eli']
print(players[2:])
#Answer: ['john', 'thomas', 'eli']

# Slicing from the end to give the last items in the list
players = ['michael','emma','john','thomas','eli']
print(players[-3:])
#Answer: ['john', 'thomas', 'eli']

#Using a Loop
players = ['michael','emma','john','thomas','eli']
print("\nThe first 3 players in the roster are:")
for player in players[0:3]:
    print(player.title())
# ANSWER:
# The first 3 players in the roster are:
# Michael
# Emma
# John