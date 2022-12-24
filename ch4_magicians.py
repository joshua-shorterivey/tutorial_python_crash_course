# Looping through entire list
#colon is required

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#doing more work within a loop 
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f'I can\'t wait to see your next trick, {magician.title()}. \n')

# do something after a for loop
print('Thank you, everyone. That was a great magic show!')

#lack of indent would throw an error
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# print(magician)

#forgetting to indent additional lines
# example of logical error, as opposed to syntax error
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
print(f'I can\'t wait to see your next trick, {magician.title()}. \n')

#unnecessary indent after the loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f'I can\'t wait to see your next trick, {magician.title()}. \n')

    print('Thank you, everyone. That was a great magic show!')