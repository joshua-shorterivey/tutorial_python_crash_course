#defining a function

def greet_user():
    """ Display a simple greeting."""
    print('Hello!')

greet_user()

# passing information to a function
def greet_user_b(username):
    """ Display a simple greeting."""
    print(f'Hello, {username} ')

greet_user_b('jesse')

#using function with a while loop
def get_formatted_name(first_name, last_name):
    '''Return a full name, neatly formatted.'''
    full_name = f'{first_name} {last_name}'
    return full_name.title()

#the following is infinite loop without the flag or break
infinite_flag = True
while infinite_flag is True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
    #infinite_flag = False

