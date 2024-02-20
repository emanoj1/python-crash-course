# Understanding Dictionaries (Ley-value pairs)

alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
print(f"The original position of alien is {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed']== 'medium':
    x_increment= 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position {alien_0['x_position']}")

# Different values in a Dictionary
favourite_languages = {
    'john': 'python',
    'jesse': 'java',
    'sam': 'c',
    'sarah':'rust'
}

language = favourite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}.")