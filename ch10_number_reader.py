"""module to learn how to load with json"""

import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)