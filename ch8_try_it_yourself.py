# 8-1. Message: Write a function called display_message() that prints one sen-
# tence telling everyone what you are learning about in this chapter. Call the
# function, and make sure the message displays correctly.
print('\n---\n8-1\n---\n')
def display_message():
    '''Prints one sentance message about chapter topic'''
    print('In this chapter I am learning about functions.')
display_message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
#  parameter, title. The function should print a message, such as One of my 
# favorite books is Alice in Wonderland. Call the function, making sure to 
# include a book title as an argument in the function call.
print('\n---\n8-2\n---\n')
def favorite_book(book):
    '''Prints message about book inputted as argument'''
    print(f'I am currently reading {book}. It is one of my favorites.')

favorite_book('Pre-suasion')

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and 
# the text of a message that should be printed on the shirt. The function 
# should print a sentence summarizing the size of the shirt and the message 
# printed on it.
# Call the function once using positional arguments to make a shirt. Call the 
# function a second time using keyword arguments.
print('\n---\n8-3\n---\n')
def make_shirt(size, text):
    '''Prints information about t-shirt order'''
    print(f'We can make you a {size} t-shirt that says \'{text}\'.')

make_shirt('large', 'cancerface')
make_shirt(size='large', text='cancerface')

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a 
# medium shirt with the default message, and a shirt of any size with a 
# different message.
print('\n---\n8-4\n---\n')
def make_shirt_b(size='large', text='I love Python'):
    '''Prints information about t-shirt order'''
    print(f'We can make you a {size} t-shirt that says \'{text}\'.')

make_shirt_b()
make_shirt_b(size='medium')
make_shirt_b('medium', 'Python is pretty cool')

# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not
# in the default country.
print('\n---\n8-5\n---\n')
def describe_city(city, country='Spain'):
    '''Prints small description of city'''
    print(f'{city} is in {country}.')

describe_city('Barcelona')
describe_city('Madrid', country='Spain')
describe_city(city='Boom', country='Belgium')

# 8-6. City Names: Write a function called city_country() that takes in the
# name of a city and its country. The function should return a string formatted
# like this:
#      "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the
# values that are returned.
print('\n---\n8-6\n---\n')
def city_country(city, country='Spain'):
    '''Prints city and country pairs'''
    print(f'{city.title()}, {country.title()}')

city_country('boom', 'belgium')
city_country('amsterdam', 'netherlands')
city_country('kartoum', 'sudan')

# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing
# different albums. Print each return value to show that the dictionaries are
# storing the album information correctly.
# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value
# for the number of songs, add that value to the album’s dictionary. Make at
# least one new function call that includes the number of songs on an album.
print('\n---\n8-7\n---\n')
def make_album(artist, title, num_tracks=None):
    '''Builds dictionary describing a music album'''
    album = {}
    album['artist'] = artist
    album['title'] = title

    if  num_tracks:
        album['number_of_tracks'] = num_tracks

    return album

print(make_album('nirvana', 'in utero'))
print(make_album(artist='helynt', title='mario & chill'))
print(make_album(artist='mikel', title='zelda & chill', num_tracks=14))

# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have
# that information, call make_album() with the user’s input and print the
# dictionary that’s created. Be sure to include a quit value in the while loop.
# print('\n---\n8-8\n---\n')
# continue_flag = True
# album_library = []
# while continue_flag:
#     artist = input('Please type the album artist? ')
#     title = input('Please type the album title? ')
#     album_library.append(make_album(artist, title))
#     print(album_library)
#     if input('Enter another album? (\'n\') to quit'):
#         continue_flag=False

# 8-9. Messages: Make a list containing a series of short text messages. Pass
# the list to a function called show_messages(), which prints each text message.
print('\n---\n8-9\n---\n')
def show_messages(message_list):
    '''Prints items of input list'''
    for message in message_list:
        print(message)

list_of_messages = ['This is the first message',
                    'This is the second message',
                    'Startling lack of creativity.']

show_messages(list_of_messages)

# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.
print('\n---\n8-10\n---\n')
def send_messages(starting_list, ending_list):
    '''Moves messages from starting to ending list'''
    while starting_list:
        message = starting_list.pop()
        print(message)
        ending_list.append(message)
    
list_of_messages = ['This is the first message',
                    'This is the second message',
                    'A Startling lack of creativity.']

sent_messages = []

send_messages(list_of_messages, sent_messages)
print(f'sent_messages = {sent_messages}')
print(f'list_of_messages = {list_of_messages}')

# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling
# the function, print both of your lists to show that the original list has
# retained its messages.
print('\n---\n8-11\n---\n')
def send_messages_b(starting_list, ending_list):
    '''Moves messages from starting to ending list'''
    while starting_list:
        message = starting_list.pop()
        print(message)
        ending_list.append(message)
    
list_of_messages = ['This is the first message',
                    'This is the second message',
                    'A Startling lack of creativity.']

sent_messages = []

send_messages_b(list_of_messages[:], sent_messages)
print(f'sent_messages = {sent_messages}')
print(f'list_of_messages = {list_of_messages}')

# 8-12. Sandwiches: Write a function that accepts a list of items a person
# wants on a sandwich. The function should have one parameter that collects as
# many items as the function call provides, and it should print a summary of
# the sand- wich that’s being ordered. Call the function three times, using a
# different num- ber of arguments each time.
print('\n---\n8-12\n---\n')
def sandwich_order(*fixings):
    '''Prints fixings on a given sandwich'''
    print(fixings)
sandwich_order('avacado', 'tomato', 'mustard')
sandwich_order('eggs', 'cheese', 'sausage', 'bacon')
sandwich_order('pickles', 'avacado', 'sirloin', 'jelly', 'mustard')

# 8-13. User Profile: Start with a copy of user_profile.py from page 149. Build
# a profile of yourself by calling build_profile(), using your first and last
# names and three other key-value pairs that describe you.
print('\n---\n8-13\n---\n')
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('shorter', 'shorter',
                            location = 'texas',
                            field = 'data_engineering',
                            age = 'old')

print(user_profile)

# 8-14. Cars: Write a function that stores information about a car in a
# diction- ary. The function should always receive a manufacturer and a model
# name. It should then accept an arbitrary number of keyword arguments. Call
# the func- tion with the required information and two other name-value pairs,
# such as a color or an optional feature. Your function should work for a call
# like this one:
#                   car = make_car('subaru', 'outback', color='blue',
# tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly.
print('\n---\n8-14\n---\n')
def make_car(manufacturer, model, **vehicle):
    """Defines information about a car"""
    vehicle['manufacturer'] = manufacturer
    vehicle['model'] = model
    return vehicle

car = make_car('kia', 'soul', color='red', drivetrain='electric', year='2019')
print(car)

# 8-15. Printing Models: Put the functions for the example printing_models.py
# in a separate file called printing_functions.py. Write an import statement at
# the top of printing_models.py, and modify the file to use the imported
# functions.
print('\n---\n8-15\n---\n')

# 8-16. Imports: Using a program you wrote that has one function in it, store
# that function in a separate file. Import the function into your main program
# file, and call the function using each of these approaches:
# import module_name
print('\n---\n8-16\n---\n')
import ch8_pizza
ch8_pizza.make_pizza(15, 'jalapeno', 'tomato')
# from module_name import function_name
from ch8_pizza import make_pizza
make_pizza('15', 'jalapeno', 'tomato')
# from module_name import function_name as fn
from ch8_pizza import make_pizza as mp
mp('15', 'jalapeno', 'tomato')
# import module_name as mn
import ch8_pizza as pizza
pizza.make_pizza('15', 'jalapeno', 'tomato')
# from module_name import *
from ch8_pizza import *
make_pizza('15', 'jalapeno', 'tomato')


# 8-17. Styling Functions: Choose any three programs you wrote for this
# chapter, and make sure they follow the styling guidelines described in this
# section.
print('\n---\n8-17\n---\n')
print('Complete')
