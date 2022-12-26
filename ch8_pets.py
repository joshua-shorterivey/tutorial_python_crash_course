#positional arguments

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f'\nI have a {animal_type}')
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

#multiple function calls
describe_pet('dog', 'willie')

#mixing up order of positional arguments
describe_pet('harry', 'hamster')

#keyword arguments
describe_pet(animal_type='hamster', pet_name='harry')

#working with default values
def describe_pet_b(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f'\nI have a {animal_type}')
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#equivalent function calls
describe_pet_b(pet_name='willie')
describe_pet_b('willie')

describe_pet_b('harry', 'hamster')
describe_pet_b(pet_name='harry', animal_type='hamster')
describe_pet_b( animal_type='hamster', pet_name='harry')

#avoiding argument errors
# describe_pet() --> missing required positional arguments
