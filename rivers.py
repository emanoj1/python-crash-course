# Print RIVERS and their Countries using Dictionary

world_rivers = {
    'river ganges': 'india',
    'river nile': 'egypt',
    'river thames': 'united kingdom',
    'the murray river': 'australia'
}

print("These are the submitted rivers of the world:")
for rivers in world_rivers.keys():
    print(rivers.title())

print("\nThese are the countries for the rivers submitted:")
for country in world_rivers.values():
    print(country.title())

print("\nThese are the rivers and their country of origin:")
for river, origin in world_rivers.items():
    print(f"{river.title()} - {origin.title()}")

# OUTPUT
# These are the submitted rivers of the world:
# River Ganges
# River Nile
# River Thames
# The Murray River

# These are the countries for the rivers submitted:
# India
# Egypt
# United Kingdom
# Australia

# These are the rivers and their country of origin:
# River Ganges - India
# River Nile - Egypt
# River Thames - United Kingdom
# The Murray River - Australia