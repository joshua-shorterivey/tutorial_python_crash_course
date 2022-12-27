#passing an arbitrary number of arguments
def make_pizza(*toppings):
    '''Print the list of topping that have been requested.'''
    #asterisk informs python to accept number of agruments into tuple
    #print(toppings) -> stage 1 of problem 
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings: #-> stage 2 of problem
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza_b(size, *toppings):
    '''Print the list of topping that have been requested.'''
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings: 
        print(f"- {topping}")

make_pizza_b(16, 'pepperoni')
make_pizza_b(12, 'mushrooms', 'green peppers', 'extra cheese')