#chapter 4: working with lists

#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these 
# pizza names in a list, and then use a for loop to print the name of each 
# pizza.
favorite_pizzas = ['cheese', 'jalapeno', 'pineapple']
for pizza in favorite_pizzas:
    print(pizza)

#• Modify your for loop to print a sentence using the name of the pizza instead 
# of printing just the name of the pizza. For each pizza you should have one 
# line of output containing a simple statement like I like pepperoni pizza.
for pizza in favorite_pizzas:
    print(f'I use to love eating {pizza} pizza.')

#• Add a line at the end of your program, outside the for loop, that states how 
# much you like pizza. The output should consist of three or more lines about 
# the kinds of pizza you like and then an additional sentence, such as I really 
# love pizza!
for pizza in favorite_pizzas:
    print(f'I use to love eating {pizza} pizza.')
print('But now that I am a vegan I rarely eat it. Sad.')

#4-2. Animals: Think of at least three different animals that have a common 
# char- acteristic. Store the names of these animals in a list, and then use a 
# for loop to print out the name of each animal.
cats = ['tiger', 'puma', 'cheetah']
for cat in cats:
    print(cat)

#• Modify your program to print a statement about each animal, such as
#A dog would make a great pet.
for cat in cats:
    print(f'{cat.title()}s are incredibly dangerous, and you should not attempt to keep one as a pet.')

#• Add a line at the end of your program stating what these animals have in 
# common. You could print a sentence such as Any of these animals would make a 
# great pet!
for cat in cats:
    print(f'{cat.title()}s are incredibly dangerous, and you should not \
    attempt to keep one as a pet.')
print('Those are all big and beautiful cats.')

print('--- End of Section ---\n')

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, 
# inclusive.
print('\n---\n4-3\n---')
for num in range(1,21):
    print(num)
# 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)
print('\n---\n4-4\n---')
# one_million = [num for num in range(1, 1_000_001)] --> code works
one_million = [num for num in range(1, 1_000_000, 50_000)]
for num in one_million:
    print(num)

# 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
print('\n---\n4-5\n---')
one_million = [num for num in range(1, 1_000_001)]
print(max(one_million))
print(min(one_million))
print(sum(one_million))

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
print('\n---\n4-6\n---')
odds = [num for num in range(1, 20, 2)]
for num in odds:
    print(num)

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
print('\n---\n4-7\n---')
three_multiples = [num for num in range(3,31) if num % 3 == 0]
for num in three_multiples:
    print(num)

# 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
print('\n---\n4-8\n---')
first_cubes = [num**3 for num in range(1, 11)]
for num in first_cubes:
    print(num)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
print('\n---\n4-9\n---')
first_cubes = [num**3 for num in range(1, 11)]

# 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
print('\n---\n4-10\n---')
players = ['charles', 'martina', 'michael', 'florence', 'eli']


#• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list. 
print('The first three items in the list are:')
print(players[:3]) 

#• Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
print('Three items middle of the list are:')
print(players[1:4])

#• Print the message The last three items in the list are:. Use a slice to print the last three items in the list.
print('The last three items in the list are:')
print(players[-3:])

#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
print('\n---\n4-11\n---')
friends_pizzas = favorite_pizzas[:]

#• Add a new pizza to the original list.
friends_pizzas.append('jalapeno & pineapple')

#• Add a different pizza to the list friend_pizzas.
friends_pizzas.append('supreme')

#• Prove that you have two separate lists. Print the message My favorite pizzas 
# are:, and then use a for loop to print the first list. Print the message My 
# friend’s favorite pizzas are:, and then use a for loop to print the second 
# list. Make sure each new pizza is stored in the appropriate list.
print('My favorite pizzas are:')
for pizza in favorite_pizzas:
    print(pizza)

print('\n')
print('My friend\'s favorite pizzas are:')
for pizza in friends_pizzas:
    print(pizza)

#4-12. More Loops: All versions of foods.py in this section have avoided using 
# for loops when printing to save space. Choose a version of foods.py, and 
# write two for loops to print each list of foods.
print('\n---\n4-12\n---')

my_foods  = ['pizza', 'falafel', 'carrot cake']
print('My favorite foods are:')
for food in my_foods:
    print(food)

friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('\nMy friend\'s favorite food are:')
for food in friend_foods:
    print(food)

# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think 
# of five simple foods, and store them in a tuple.
print('\n---\n4-13\n---')
menu = ('pizza', 'falafel', 'carrot cake', 'cannoli', 'hamburger')

#• Use a for loop to print each food the restaurant offers.
for item in menu:
    print(item)

#• Try to modify one of the items, and make sure that Python rejects the change.
# menu[0] = 'pasta'

#• The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.
menu = ('pizza', 'falafel', 'pasta', 'cannoli', 'lasagna')
for item in menu:
    print(item)

# 4-14. PEP 8: Look through the original PEP 8 style guide at
# https://python.org/dev/peps/pep-0008/. You won’t use much of it now, but it
# might be interesting to skim through it.

# 4-15. Code Review: Choose three of the programs you’ve written in this
# chapter and modify each one to comply with PEP 8:

#• Use four spaces for each indentation level. Set your text editor to insert
# four spaces every time you press tab, if you haven’t already done so (see
# Appendix B for instructions on how to do this).

#• Use less than 80 characters on each line, and set your editor to show a
# vertical guideline at the 80th character position.

# • Don’t use blank lines excessively in your program files.
