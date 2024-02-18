alien_color = 'green'

if alien_color == 'green':
    got_points = 5
elif alien_color == 'yellow':
    got_points = 10
elif alien_color == 'red':
    got_points = 15

print(f"Version1: You got {got_points} points!")

# Another version
alien_color = ['green','yellow','red']

color = 'green'

if color == 'green':
    got_points = 5
elif color == 'yellow':
    got_points = 10
elif color == 'red':
    got_points = 15

print(f"Version2: You got {got_points} points!")