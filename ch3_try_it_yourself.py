## Try It Yourself ##

# Try these short programs to get some firsthand experience with Python’s lists. You might want to create a new folder for each chapter’s exercises to keep them organized.

# 3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
friends = ['alan', 'herman', 'chochise', 'kurt']
print(friends[-1])
print(friends[0])
print(friends[1])
print(friends[-2])

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.
print(f'Hello, {friends[-1].title()}. It\'s good to see you again')
print(f'Hello, {friends[-0].title()}. It\'s good to see you again')
print(f'Hello, {friends[1].title()}. It\'s good to see you again')
print(f'Hello, {friends[-2].title()}. It\'s good to see you again')

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
car_attributes = ['Honda', 'Electric', 'Kia', 'Lexus']

print(f'I have never driven a {car_attributes[-1]} car.')
print(f'I have owned multiple {car_attributes[0]} cars.')
print(f'I would like to own an {car_attributes[1]} car.')
print(f'I like to rent {car_attributes[2]} cars.')

print('--- End of Section ---\n')
# The following exercises are a bit more complex than those in Chapter 2, but they give you an opportunity to use lists in all of the ways described.

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
guest_list=['Alan Turing', 'Harvey Milk', 'Brittney Griner']
for person in guest_list:
    print(f'Hello {person}, would you like to join us for dinner tonight?')


# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

# • Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
print(f'{guest_list[-1]} can\'t make it. We need to invite someone else.')

# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
guest_list[-1] = 'Carli Lloyd'

# • Print a second set of invitation messages, one for each person who is still in your list.
for person in guest_list:
    print(f'Hello {person}, would you like to join us for dinner tonight?')

# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table.
print('Hello everyone, we have found a bigger dinner table.')

#• Use insert() to add one new guest to the beginning of your list.
guest_list.insert(0, 'Ursula von der Leyen')

#• Use insert() to add one new guest to the middle of your list.
guest_list.insert(2, 'MaryAnne Adams')

#• Use append() to add one new guest to the end of your list.
guest_list.append('Megan Rapinoe')

#• Print a new set of invitation messages, one for each person in your list.
print('\nNew Invitations\n---')
for person in guest_list:
    print(f'Hello {person}, would you like to join us for dinner tonight?')

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
print('\nChange of plans. We can only invite two people now. Apologies for the inconvenience.')

#• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
while len(guest_list) != 2:
    disinvited = guest_list.pop()
    print(f'Sorry, {disinvited}. We\'ve had to make some extreme changes to the guest list.')

#• Print a message to each of the two people still on your list, letting them know they’re still invited.
for person in guest_list:
    print(f'Hello {person}, we have been ablel to secure you place at dinner. Would you still like to join us?')

#• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
del guest_list[1]
del guest_list[0]

print(guest_list)

print('\n --- End of Section --- \n')

# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
#• Store the locations in a list. Make sure the list is not in alphabetical order.
places_to_visit = ['Sweden', 'Dominican Republic', 'Antartica', 'South Korea', 'China']

#• Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
print(places_to_visit)
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(places_to_visit))

#• Show that your list is still in its original order by printing it.
print(places_to_visit)
#• Use sorted() to print your list in reverse alphabetical order without chang- ing the order of the original list.
print(sorted(places_to_visit, reverse=True))

#• Show that your list is still in its original order by printing it again.
print(places_to_visit)

#• Use reverse() to change the order of your list. Print the list to show that its order has changed.
places_to_visit.reverse()
print(places_to_visit)

#• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
places_to_visit.reverse()
print(places_to_visit)

#• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
places_to_visit.sort()
print(places_to_visit)

#• Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
places_to_visit.sort(reverse=True)
print(places_to_visit)
# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 42), use len() to print a message indicating the number of people you are inviting to dinner.
print(len(guest_list))

# 3-10. Every Function: Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or any- thing else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

#functions to use: append, insert, del, pop, remove, sort, reverse, sorted, len 
planets = ['mercury', 'venus', 'earth', 'jupiter', 'saturn', 'uranus', 'neptune']
print(planets)
planets.append('pluto')
print(planets)
planets.insert(3, 'mars')
print(planets)
del planets[0]
print(planets)
planets.pop(-1)
print(planets)
planets.remove('venus')
print(planets)
planets.sort()
print(planets)
planets.reverse()
print(planets)
print(sorted(planets))
print(len(planets ))

print('\n--- End of Section ---\n')


#3-11. Intentional Error: If you haven’t received an index error in one of your programs yet, try to make one happen. Change an index in one of your pro- grams to produce an index error. Make sure you correct the error before clos- ing the program.

# print(planets[6]) #-> throws index out of range error