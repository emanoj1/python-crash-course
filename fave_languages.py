# Using FOR LOOP in a DICTIONARY

fave_languages = {
    'sarah': 'python',
    'tom': 'javascript',
    'chelsea': 'flask',
    'tim': 'postgresql',
    'john': 'python',
    'hector': 'python',
    'jessica': 'flask',
    'emma': 'javascript'

}

for person, language in fave_languages.items():
    print(f"{person.title()} favorite programming language is {language.title()}")

#OUTPUT
# Sarah favorite programming language is Python
# Tom favorite programming language is Javascript
# Chelsea favorite programming language is Flask
# Tim favorite programming language is Postgresql

print(f"\nThese people like programming:")    
for name in fave_languages.keys():
    print(name.title())

#OUTPUT
#These people like programming:
#Sarah
#Tom
#Chelsea
#Tim

# Specific message to items in a dictionary
friends = ['tom', 'chelsea']
for name in fave_languages:
    print(f"\nHey {name.title()}")

    if name in friends:
        language = fave_languages[name].title()
        print(f"\t{name.title()}, you polled and you love {language.title()}. Thanks!")

if 'erin' not in fave_languages:
    print(f"\nErin, you need to poll please")

# Print only the VALUES
print("\nThese are the languages that users submitted:")
for polled_language in fave_languages.values():
    print(polled_language.title())

# OUTPUT
# These are the languages that users submitted:
# Python
# Javascript
# Flask
# Postgresql
# Python
# Python
# Flask
# Javascript

#Print UNIQUE Values only

print("\nThese are the UNIQUE values of languages submitted:")
for polled_language in set(fave_languages.values()):
    print(polled_language.title())

# OUTPUT
# These are the UNIQUE values of languages submitted:
# Postgresql
# Python
# Javascript
# Flask  