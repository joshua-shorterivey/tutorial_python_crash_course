#importing multiple classes from module
from ch9_car import Car, ElectricCar

my_beetle = Car('vokswagen', 'bettle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

#via entire module importation
import ch9_car as c

my_beetle = c.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = c.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

from ch9_electric_car import ElectricCar_b as EC
my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())