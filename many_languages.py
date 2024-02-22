#Nesting a list in a Dictionary

#Store the info
fave_languages = {
    'matt': ['python','javascript'],
    'melissa': ['flask','mongodb','postgresql'],
    'henry': ['postgresql'],
    'timmoty': ['html','css'],
    'teresa': ['react','c++'],
    'nancy': ['python']
}

# List languages known per person
for person, languages in fave_languages.items():
    #Check if someone only knows 1 language
    only_one = len(languages)
    if only_one == 1:
        print(f"\n{person.title()} knows only 1 language {language.title()}")
    else:
        #For those who know many languages
        print(f"\n{person.title()} knows these languages:")
        for language in languages:
            print(f"\t{language.title()}")

# OUTPUT
# Matt knows these languages:
#         Python
#         Javascript

# Melissa knows these languages:
#         Flask
#         Mongodb
#         Postgresql

# Timmoty knows these languages:
#         Html
#         Css

# Teresa knows these languages:
#         React
#         C++

# Nancy knows only 1 language C++