# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.
print('\n---\n6-1\n---\n')
person = {'first_name': 'alan', 'last_name': 'turing', 'city': 'manchester', \
        'age': 110}
for item in person.items():
    #.items() returns tuple -> (key, value)
    print(item[1])

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
print('\n---\n6-2\n---\n')
# Think of five names, and use them as keys in your dictionary. Think of a
# favorite number for each person, and store each as a value in your
# dictionary. Print each person’s name and their favorite number. For even more
# fun, poll a few friends and get some actual data for your program.
names_numbers = {'charles': 38, 'martina':27, 'michael':8, 'florence':19,\
                'eli':6}

for person in names_numbers.items():
    print(f'{person[0].title()}\'s favorite number is {person[1]}.')

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
print('\n---\n6-3\n---\n')
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
glossary = {'variable': 'container that stores given value',\
            'string': 'a series of characters' ,\
            'list': 'a collection of items in a particular order', \
            'integer': 'positive and negative whole numbers' ,\
            'if-else': 'syntax for executing code based on certain conditions' }
# • Print each word and its meaning as neatly formatted output. You might print
# the word followed by a colon and then its meaning, or print the word on one
# line and then print its meaning indented on a second line. Use the newline
# character (\n) to insert a blank line between each word-meaning pair in your
# output.
for word in glossary.items():
    print (f'Word: {word[0]}\nMeaning: {word[1]}\n---')

# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up
# the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.
print('\n---\n6-4\n---\n')
glossary['class'] = 'a template for creating user-defined objects'
glossary['CPython'] = 'the canonical implementation of Python in C'
glossary['floor division'] = 'division that rounds the result down to the \
                             nearest integer'
glossary['comments'] = 'lines of code that will not be executed'
glossary['iterator'] = 'an object that contains a countable number of values'

for word in glossary.items():
    print (f'Word: {word[0]}\nMeaning: {word[1]}\n---')

# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
print('\n---\n6-5\n---\n')
major_rivers = {'nile': 'egypt', 'rhine': 'germany', 'colorado': 'usa'}

# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
for river in major_rivers.items():
    print (f'The {river[0].title()} river runs through {river[1].title()}.')

# • Use a loop to print the name of each river included in the dictionary.
for river in major_rivers.keys():
    print(river)

# • Use a loop to print the name of each country included in the dictionary.
for river in major_rivers.values():
    print(river)
    
# 6-6. Polling: Use the code in favorite_languages.py (page 97).
print('\n---\n6-6\n---\n')
# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.


# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
print('\n---\n6-7\n---\n')

# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As
# you loop through the list, print everything you know about each person.

# 6-8. Pets: Make several dictionaries, where each dictionary represents a
# differ- ent pet. 
print('\n---\n6-8\n---\n')

# • In each dictionary, include the kind of animal and the owner’s name. Store
# these dictionaries in a list called pets. 
# • Next, loop through your list and as you do, print everything you know about
# each pet.


# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of
# three names to use as keys in the dictionary, and store one to three favorite
# places for each person. To make this exercise a bit more interesting, ask
# some friends to name a few of their favorite places. Loop through the
# dictionary, and print each person’s name and their favorite places.
print('\n---\n6-9\n---\n')

# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99) so
# each person can have more than one favorite number. Then print each
# person’s name along with their favorite numbers.
print('\n---\n6-10\n---\n')

# 6-11. Cities: Make a dictionary called cities. Use the names of three cities
# as keys in your dictionary. Create a dictionary of information about each
# city and include the country that the city is in, its approximate population,
# and one fact about that city. The keys for each city’s dictionary should be
# something like country, population, and fact. Print the name of each city and
# all of the infor- mation you have stored about it.
print('\n---\n6-11\n---\n')

# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example
# programs from this chapter, and extend it by adding new keys and values,
# chang- ing the context of the program or improving the formatting of the
# output.
print('\n---\n6-12\n---\n')