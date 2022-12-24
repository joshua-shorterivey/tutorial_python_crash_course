#tuples

#defining a tuple
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#attempting to reassign value --> will throw an error
# dimensions[0] = 250

#generating tuple with single element --> presence of comma ensures tuple type
my_tuple = (3,)
print(my_tuple)

#looping through tuple
for dimension in dimensions:
    print(dimension)

#writing over a tuple
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)