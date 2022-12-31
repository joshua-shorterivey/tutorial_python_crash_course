"""module teaching write file operations"""
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    #does not automatically append as new line
    file_object.write("I love creating new games")

#include newlines in the calls
with open(filename, 'w') as file_object:
    file_object.write("I love programming\n")
    file_object.write("I love creating new games\n")

#appending to file
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

