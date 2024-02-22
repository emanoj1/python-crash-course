#A LIST of dictionaries

# alien_0 = {'color': 'green', 'points': '5'}
# alien_1 = {'color': 'yellow', 'points': '10'}
# alien_2 = {'color': 'red', 'points': '15'}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

aliens = []

for alien_number in range(10):
    new_alien = {'color': 'green', 'points': 5, 'speed':'slow'}
    aliens.append(new_alien)


print(f"Total aliens in list {len(aliens)}")

for alien in aliens[:3]: # only the first 3, use Splice method
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens[:5]: #show only the first 5, use Splice method
    print(alien)