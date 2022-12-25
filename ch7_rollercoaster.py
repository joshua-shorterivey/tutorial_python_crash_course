
#using int() to accept numerical input
age = input('How old are you ? ')
print(age)
print(type(age))

#this will throw error. unorderable types: str() >= int()
#age >= 18

#this will cast the variable as an integer
age = int(age)
print(age >= 18)

height = input('How tall are you, in inches? ')
height = int(height)

if height >= 48:
    print('\nYou\'re tall enough to ride')
else:
    print('\nYou\'ll be able to ride when you\'re a little older.')