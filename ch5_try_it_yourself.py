# --- Chapter 5: Try It Yourself ---

#5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your
# code should look something like this:
print('\n---\n5-1\n---')
#                   car = 'subaru'
#                   print("Is car == 'subaru'? I predict True.")
#                   print(car == 'subaru')
#                   print("\nIs car == 'audi'? I predict False.")
#                   print(car == 'audi')
fav_number = 19
print('Is fav_number = 18? I predict False')
print(fav_number == 18)

print('Is fav_number + 2 == 21? I predict True')
print(fav_number + 2 == 21)

# • Look closely at your results, and make sure you understand why each line
# evaluates to True or False.

# • Create at least ten tests. Have at least five tests evaluate to True and
# another five tests evaluate to False.
print('Does isinstance(fav_number, int) return True? Yes')
print(isinstance(fav_number, int))

print('Is str(fav_number) == \'19\'? I predict True')
print(str(fav_number) == '19')

print('Does isinstance(fav_number/2, int) return True? No')
print(isinstance(fav_number/2, int))

# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to ten. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:
print('\n---\n5-2\n---')

# • Tests for equality and inequality with strings
print('Is \'first\' == \'first\'?')
print('first' == 'first')

# • Tests using the lower() method
print('Is \'First\'.lower() == \'First\'?')
print('First'.lower() == 'First')

# • Numerical tests involving equality and inequality, greater than and less
# than, greater than or equal to, and less than or equal to
print('Is 2 > 1?')
print(2 > 1)

print('Is 2 < 1?')
print(2 < 1)

print('Does 2 != 1?')
print(2 != 1)

print('False is True?')
print(False is True)

print('Is 22 <= (2*11)?')
print(22 <= (2*11))

print('Is 33 >= (2*11)?')
print(33 >= (2*11))

# • Tests using the and keyword and the or keyword
print('True and False?')
print(True and False)

# • Test whether an item is in a list
menu = ['pizza', 'pasta', 'french fries', 'udon', 'brussel sprouts']
print(f'The menu is: {menu}')
print('Is kale on the menu?')
print('kale' in menu)

# • Test whether an item is not in a list
print('Are hamburgers not on the menu?')
print('hamburgers' not in menu)

# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
# variable called alien_color and assign it a value of 'green', 'yellow', or
# 'red'.
print('\n---\n5-3\n---')
alien_color = 'red'

# • Write an if statement to test whether the alien’s color is green. If it is,
# print a message that the player just earned 5 points.
if alien_color == 'green':
    print('The player has earned 5 points')

# • Write one version of this program that passes the if test and another that
# fails. (The version that fails will have no output.)
alien_color = 'green'
if alien_color == 'green':
    print('The player has earned 5 points')

alien_color = 'blue'
if alien_color == 'green':
    print('The player has earned 5 points')


# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3,
# and write an if-else chain.
print('\n---\n5-4\n---')

# • If the alien’s color is green, print a statement that the player just
# earned 5 points for shooting the alien.
alien_color = 'green'
if alien_color == 'green':
    print('The player has earned 5 points')

# • If the alien’s color isn’t green, print a statement that the player just
# earned 10 points.
alien_color = 'green'
if alien_color == 'green':
    print('The player has earned 5 points')
else:
    print('The player has earned 10 points')

# • Write one version of this program that runs the if block and another that
# runs the else block.
alien_color = 'green'
if alien_color == 'green':
    print('The player has earned 5 points')
else:
    print('The player has earned 10 points')


alien_color = 'blue'
if alien_color == 'green':
    print('The player has earned 5 points')
else:
    print('The player has earned 10 points')

# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an
# if-elif- else chain.
print('\n---\n5-5\n---')

# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
alien_color = 'red'
if alien_color == 'green':
    print('The player has earned 5 points')
elif alien_color == 'yellow':
    print('The player has earned 10 points')
else:
    print('The player has earned 15 points')
    
# • Write three versions of this program, making sure each message is printed
# for the appropriate color alien.
alien_color = 'green'
if alien_color == 'green':
    print('The player has earned 5 points')
elif alien_color == 'yellow':
    print('The player has earned 10 points')
else:
    print('The player has earned 15 points')

alien_color = 'yellow'
if alien_color == 'green':
    print('The player has earned 5 points')
elif alien_color == 'yellow':
    print('The player has earned 10 points')
else:
    print('The player has earned 15 points')

# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
# stage of life. Set a value for the variable age, and then:
print('\n---\n5-6\n---')
AGE = 47
# • If the person is less than 2 years old, print a message that the person is
#  a baby.
if AGE < 2:
    print('That person is a baby!')
# • If the person is at least 2 years old but less than 4, print a message that
#  the person is a toddler.
elif AGE < 4:
    print('That person is a toddler!')
# • If the person is at least 4 years old but less than 13, print a message
# that the person is a kid.
elif AGE < 13:
    print('That person is a kid!')
# • If the person is at least 13 years old but less than 20, print a message
# that the person is a teenager.
elif AGE < 20:
    print('That person is a teenager!')
# • If the person is at least 20 years old but less than 65, print a message
# that the person is an adult.
elif AGE < 65:
    print('That person is an adult!')
# • If the person is age 65 or older, print a message that the person is an elder.
elif AGE >= 65:
    print('That person is an elder!')

# ------------#
# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a
# series of independent if statements that check for certain fruits in your list.
print('\n---\n5-7\n---')
# • Make a list of your three favorite fruits and call it favorite_fruits.
favorite_fruits = ['bananas', 'cherries', 'avacados']
# • Write five if statements. Each should check whether a certain kind of fruit
# is in your list. If the fruit is in your list, the if block should print a
# statement, such as You really like bananas!
if 'bananas' in favorite_fruits:
    print('You really like bananas!')

if 'mangos' in favorite_fruits:
    print('You really like mangos!')

if 'blueberries' in favorite_fruits:
    print('You really like blueberries!')

if 'cherries' in favorite_fruits:
    print('You really like cherries!')

if 'strawberries' in favorite_fruits:
    print('You really like strawberries!')

# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting
# to each user:
print('\n---\n5-8\n---')
user_names = ['admin', 'gloryboy', 'testy', 'pesty', 'flexy']
# • If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# • Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
for user in user_names:
    if user == 'admin':
        print(f'Hello {user}, would you like to see a status report?')
    else:
        print(f'Hello {user}, thank you for logging in again.')

# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
print('\n---\n5-9\n---')
for user in user_names.copy():
    user_names.remove(user)

# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct
# message is printed.
if len(user_names) == 0:
    print('We need to find some users!')

# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
print('\n---\n5-10\n---')

# • Make a list of five or more usernames called current_users.
current_users = ['Admin', 'GloryBoy', 'testy', 'pesty', 'flexy']

# • Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.
new_users = ['fleafly', 'gloryboy', 'manticore', 'ArrowFlex', 'gamewar']

# • Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying that
# the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
# current_users containing the lowercase versions of all existing users.)
current_copy = [x.casefold() for x in current_users]

for user in new_users:
    if user in current_copy:
        print(f'The username: {user} is unavailable. Please choose another name.')
    else:
        print(f'The username: {user} is available.')

# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list,
# such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
print('\n---\n5-11\n---')

# • Store the numbers 1 through 9 in a list.
ordinal_list = list(range(1,10))
print(ordinal_list)
# • Loop through the list.
# • Use an if-elif-else chain inside the loop to print the proper ordinal end-
# ing for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th
# 9th", and each result should be on a separate line.
for num in ordinal_list:
    if num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')
    elif num in [4,5,6,7,8,9]:
        print(f'{num}th')
    
# 5-12. Styling if statements: Review the programs you wrote in this chapter,
# and make sure you styled your conditional tests appropriately.
print('\n---\n5-12\n---')



# 5-13. Your Ideas: At this point, you’re a more capable programmer than you
# were when you started this book. Now that you have a better sense of how
# real-world situations are modeled in programs, you might be thinking of some
# problems you could solve with your own programs. Record any new ideas you have
# about problems you might want to solve as your programming skills continue
# to 
# improve. Consider games you might want to write, data sets you might want to
# explore, and web applications you’d like to create.

# I want to make a platformer