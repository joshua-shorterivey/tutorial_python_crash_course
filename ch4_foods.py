#copying a list

my_foods  = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print('My favorite foods are:')
print(my_foods)

print('\nMy friend\'s favorite food are:')
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)

print('\nMy friend\'s favorite food are:')
print(friend_foods)

# this doesn't work: --> points to same list in memory
my_foods  = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)

print('\nMy friend\'s favorite food are:')
print(friend_foods)