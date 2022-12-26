# 7-1. Rental Car: Write a program that asks the user what kind of rental car
# they would like. Print a message about that car, such as “Let me see if I can
# find you a Subaru.”
# print('\n---\n7-1\n---\n')
# car_request = input('What kind of rental car would you like? ')
# print(f'Let me see if I can find you a {car_request}.')

# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message
# saying they’ll have to wait for a table. Otherwise, report that their table
# is ready.
print('\n---\n7-2\n---\n')
group_size = int(input('How many people are in your dinner group? '))

if group_size > 8:
    print('Sorry, you will have to wait for a table.')
else: 
    print('Your table is ready.')

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.
print('\n---\n7-3\n---\n')
is_multiple_of_10 = int(input('Please enter a number: '))
if is_multiple_of_10 % 10 == 0:
    print('This is a multiple of 10.')
else: 
    print('This is not a multiple of 10')

# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping
# print a message saying you’ll add that topping to their pizza.
print('\n---\n7-3\n---\n')
keep_going = True
toppings = []
while keep_going is True:
    topping = input("What topping would you like to add? ")
    if topping == 'quit':
        keep_going = False
    else:
        toppings.append(topping)
        print(f'We will add {topping} to your pizza.')
print(toppings)

# 7-5. Movie Tickets: A movie theater charges different ticket prices depending
# on a person’s age. If a person is under the age of 3, the ticket is free; if
# they are between 3 and 12, the ticket is $10; and if they are over age 12,
# the ticket is $15. Write a loop in which you ask users their age, and then
# tell them the cost of their movie ticket.
print('\n---\n7-5\n---\n')
keep_going = True

while keep_going is True:
    age = input("What is your age?")
    if age == 'quit':
        keep_going = False
    elif int(age) < 3:
        print('Their ticket is free')
    elif int(age) <= 12:
        print('The ticket is $10')
    elif int(age) > 12:
        print('The ticket is $15')

# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise
# 7-5 that do each of the following at least once:
print('\n---\n7-3\n---\n')
# • Use a conditional test in the while statement to stop the loop.
keep_going = True

while keep_going is True:
    age = input("What is your age?")
    if age == 'quit':
        keep_going = False
    elif int(age) < 3:
        print('Their ticket is free')
    elif int(age) <= 12:
        print('The ticket is $10')
    elif int(age) > 12:
        print('The ticket is $15')
# • Use an active variable to control how long the loop runs.
i=0
while i < 1:
    age = input("What is your age?")
    if int(age) < 3:
        print('Their ticket is free')
    elif int(age) <= 12:
        print('The ticket is $10')
    elif int(age) > 12:
        print('The ticket is $15')
    i+= 1
# • Use a break statement to exit the loop when the user enters a 'quit' value.
keep_going = True

while keep_going is True:
    age = input("What is your age?")
    if age == 'quit':
        break
    if int(age) < 3:
        print('Their ticket is free')
    elif int(age) <= 12:
        print('The ticket is $10')
    elif int(age) > 12:
        print('The ticket is $15')

# 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop
# press ctrl-C or close the window displaying the output.)
print('\n---\n7-7\n---\n')

# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of
# vari- ous sandwiches. Then make an empty list called finished_sandwiches.
# Loop through the list of sandwich orders and print a message for each order
# such as I made your tuna sandwich. As each sandwich is made, move it to the
# list of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.
print('\n---\n7-8\n---\n')
sandwich_orders = ['rueben', 'blt', 'hamburger', 'avacado']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('I have made your {}.'.format(sandwich))
    finished_sandwiches.append(sandwich)

print("Today we made an {}, a {}, {}, and a {} sandiwch."\
        .format(finished_sandwiches[0],
                finished_sandwiches[1],
                finished_sandwiches[2],
                finished_sandwiches[3]))
    

# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has run
# out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in
# finished_sandwiches.
print('\n---\n7-9\n---\n')
sandwich_orders = ['rueben', 'blt', 'hamburger','pastrami', 'pastrami',
                   'avacado', 'pastrami']
finished_sandwiches = []

print('The deli has run out of pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('I have made your {}.'.format(sandwich))
    finished_sandwiches.append(sandwich)

print('Today we made the following sandwiches: ')
for sandwich in finished_sandwiches:
    print(f'A {sandwich}')

# 7-10. Dream Vacation: Write a program that polls users about their dream
# vacation. Write a prompt similar to If you could visit one place in the
# world, where would you go? Include a block of code that prints the results of
# the poll.
print('\n---\n7-10\n---\n')
polling_active = True
results = {}

while polling_active:
    name = input("Please enter your name? ")
    destination = input("Where would you like to go? ")
    results[name] = destination

    next_up = input("Is there anyone else that would like to enter a location? "
                    "(yes/no)")
    if next_up == 'no':
        polling_active = False

for person in results.items():
    print(f"{person[0]} would like to go to {person[1]}. ")
