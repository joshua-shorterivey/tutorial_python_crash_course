import ch8_pizza

ch8_pizza.make_pizza(16, 'pepperoni')
ch8_pizza.make_pizza(12, 'musrooms', 'green peppers', 'extra cheese')


from ch8_pizza import make_pizza
#from ch8_pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'musrooms', 'green peppers', 'extra cheese')

from ch8_pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'musrooms', 'green peppers', 'extra cheese')

import ch8_pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'musrooms', 'green peppers', 'extra cheese')