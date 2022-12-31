"""module continuing work on saving/loading user data"""

import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}")