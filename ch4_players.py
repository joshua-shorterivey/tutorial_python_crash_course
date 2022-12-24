# working with part of a list

#slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

#working with different subset of list
print(players[1:4])

#omitting first index of slice
print(players[:4])

#omitting last index of slice
print(players[2:])

#using negative indexing
print(players[-3:])

#looping through a slice
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())

