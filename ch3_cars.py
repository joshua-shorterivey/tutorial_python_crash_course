
#sorting alist permanenetly with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#sorting in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#sorting list temporarily
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the original List:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)

#printing list in reverse order
print(cars)
cars.reverse()
print(cars)


#finding length of list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
