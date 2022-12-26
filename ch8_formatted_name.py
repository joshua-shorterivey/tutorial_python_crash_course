#returning a simple value
def get_formatted_name(first_name, last_name):
    '''Return a full name, neatly formatted.'''
    full_name = f'{first_name} {last_name}'
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#making an argument optional
def get_formatted_name_b(first_name, middle_name, last_name):
    '''Return a full name, neatly formatted.'''
    full_name = f'{first_name} {middle_name} {last_name}'
    return full_name.title()

musician = get_formatted_name_b('john','lee', 'hooker')
print(musician)

def get_formatted_name_c(first_name, last_name, middle_name=''):
    '''Return a full name, neatly formatted.'''
    if middle_name: #-> empty string evaluates as false
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()

musician = get_formatted_name_c('jimi', 'hendrix')
print(musician)

musician = get_formatted_name_c('john','hooker', 'lee')
print(musician)

