"""opens file containing first 30 digits of pi"""
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
print(contents.rstrip())

#using relative path
#with open(text_files/filename.txt') as file_object:

#using absolute path with variable assignment
#file_path = '/home/some_folder/other_files/text_files/filename.txt'
#with open(file_path) as file_object:

#reading line by line
filename = 'pi_digits.txt'

with open(filename) as file_object:
        for line in file_object:
            #place .rstrip to remove excess newline chars
            print(line.rstrip())

#making a list of lines from a file
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())