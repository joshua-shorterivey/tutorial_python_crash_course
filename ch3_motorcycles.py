
# modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#adding elements to list 
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

#instantizes an empty list
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

#insert elements into a list
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)


#removing elements from list using del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

#using pop method to retain removed item in different variable
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print(f'The last motorcycle I owned was a {popped_motorcycle.title()}.')

#popping from any position in the list
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f'The first motorcylcle I owned was a {first_owned.title()}.')

#removing an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#using remove mothod
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)

print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')


#avoided errors. 
motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3]) --> will throw an error
print(motorcycles[-1]) #-> best way to access last item in list. do not use with empty list