#returning a dictionary
def build_person(first_name, last_name):
    '''Return a dictionary of information about a person.'''
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

#adding optional values
def build_person_b(first_name, last_name, age=None):
    '''Return a dictionary of information about a person.'''
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person_b('jimi', 'hendrix', age=27)
print(musician)