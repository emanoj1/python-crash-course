# Using FOR LOOP in a DICTIONARY

fave_languages = {
    'sarah': 'python',
    'tom': 'javascript',
    'chelsea': 'flask',
    'tim': 'postgresql'
}

for person, language in fave_languages.items():
    print(f"{person.title()} favorite programming language is {language.title()}")

#OUTPUT
# Sarah favorite programming language is Python
# Tom favorite programming language is Javascript
# Chelsea favorite programming language is Flask
# Tim favorite programming language is Postgresql