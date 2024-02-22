#Challenge 6-7 People, page 111
# using Dictionary in a Dictionary

people = {
    'mvincent': {
        'first_name': 'manny',
        'last_name': 'vincent',
        'age': 45,
        'location': 'sydney'
        },

    'hjoseph':{
        'first_name': 'hector',
        'last_name': 'joseph',
        'age': '57',
        'location': "melbourne" 
    }
}

for person, details in people.items():
    print(f"\nThe full details of {person} are:")
    print(f"\tFirst Name: {details['first_name'].title()}")
    print(f"\tLast Name: {details['last_name'].title()}")
    print(f"\tage: {details['age']}")
    print(f"\tLocation: {details['location'].title()}")