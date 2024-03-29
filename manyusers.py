users = {
    'aeistein': {
        'first_name': 'albert',
        'second_name': 'einstein',
        'location': 'usa',
    },

    'mcurie': {
        'first_name': 'marie',
        'second_name': 'curie',
        'location': 'france'
    }
}

for username, user_info in users.items():
    print(f"Username:,{username}")
    full_name = f"{user_info['first_name']} {user_info['second_name']}"
    location = f"{user_info['location']}"
    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.upper()}")