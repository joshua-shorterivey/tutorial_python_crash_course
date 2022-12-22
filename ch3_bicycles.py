#creating a list
bicycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles)

#accessing elements in a list. zero indexed 
print(bicycles[0])
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

#accessing element and using string method
print(bicycles[0].title())

#using indicidual values from a list
message = f'My first bicyel was a {bicycles[0].title()}.'
print(message)