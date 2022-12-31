"""this is a module holding the chapter 10 try-it-yourself exercises"""
# 10-1. Learning Python: Open a blank file in your text editor and write a few 
# lines summarizing what you’ve learned about Python so far. Start each line 
# with the phrase In Python you can. . . . Save the file as learning_python.txt 
# in the same directory as your exercises from this chapter. Write a program 
# that reads the file and prints what you wrote three times. Print the contents 
# once by reading in the entire file, once by looping over the file object, and once by storing the lines in a list and then working with them outside the with block.
print('\n---\n10-1\n---')
filename = 'learning_python.txt'
with open(filename) as f:
    text = f.read()
    print(text)

print('\n')
with open(filename) as f:
    for line in f:
        print(line)

print('\n')
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line)

# 10-2. Learning C: You can use the replace() method to replace any word in a 
# string with a different word. Here’s a quick example showing how to replace 
# 'dog' with 'cat' in a sentence:
# >>> message = "I really like dogs." 
# >>> message.replace('dog', 'cat') 
# 'I really like cats.'
# Read in each line from the file you just created, learning_python.txt, and 
# replace the word Python with the name of another language, such as C. Print 
# each modified line to the screen.
print('\n---\n10-2\n---')
with open(filename) as f:
    for line in f:
        print(line.replace('Python','Ruby'))

# 10-3. Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.
print('\n---\n10-3\n---')
filename = 'guest.txt'

# with open(filename, 'w') as f:
#     guest_name = input("What is your name? ")
#     f.write(guest_name)

# 10-4. Guest Book: Write a while loop that prompts users for their name. When
# they enter their name, print a greeting to the screen and add a line
# recording their visit in a file called guest_book.txt. Make sure each entry
# appears on a new line in the file.
print('\n---\n10-4\n---')
filename = 'guest_book.txt'
loop_flag = True

with open(filename, 'w') as f:
    while loop_flag:
        name = input("Please input your name: (q to quit)")
        if name == 'q':
            break
        print(f'Welcome, {name.title()}.')
        f.write(name.title()+'\n')


# 10-5. Programming Poll: Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a file
# that stores all the responses.
print('\n---\n10-5\n---')
filename = 'poll_responses.text'

with open(filename, 'a') as f:
    while True:
        rationale = input("Why do you like programming? (q to quit) ")
        if rationale == 'q':
            break
        f.write(rationale.capitalize()+'\n')

# 10-6. Addition: One common problem when prompting for numerical input occurs
# when people provide text instead of numbers. When you try to convert the
# input to an int, you’ll get a ValueError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the ValueError if
# either input value is not a number, and print a friendly error message. Test
# your program by entering two numbers and then by entering some text instead
# of a number.
print('\n---\n10-6\n---')
print("Input two numbers in numerical form. Enter 'q' to quit. ")

while True:
    first_number = input('Enter the first number: ')
    if first_number == 'q':
        break
    else:
        try:
            first_number = int(first_number)
        except ValueError:
            print('Please enter the numerical form')
        else:
            try:
                second_number = int(input('Enter the second number: '))
                if second_number == 'q':
                    break
            except ValueError:
                print('Please enter the numerical form')
            else:
                sum = first_number + second_number
                print(f"{first_number} + {second_number} is {sum}")


# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number.
print('\n---\n10-7\n---')
print("Input two numbers in numerical form. Enter 'q' to quit. ")

while True:
    first_number = input('Enter the first number: ')
    if first_number == 'q':
        break

    second_number = input('Enter the second number: ')
    if first_number == 'q':
        break

    try:
        first_number = int(first_number)
    except ValueError:
        print('Please enter the numerical form')
    else:
        try:
            second_number = int(second_number)
        except ValueError:
            print('Please enter the numerical form')
        else:
            sum = first_number + second_number
            print(f"{first_number} + {second_number} is {sum}")


# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least
# three names of cats in the first file and three names of dogs in the second
# file. Write a program that tries to read these files and print the contents
# of the file to the screen. Wrap your code in a try-except block to catch the
# FileNotFound error, and print a friendly message if a file is missing. Move
# one of the files to a dif- ferent location on your system, and make sure the
# code in the except block executes properly.
print('\n---\n10-8\n---')
filenames = ['cats.txt', 'dogs.txt', 'animals.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print(f'Sorry. That file, {filename}, does not exist')

# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
# silently if either file is missing.
print('\n---\n10-9\n---')
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        pass

# 10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org/ ) and
# find a few texts you’d like to analyze. Download the text files for these
# works, or copy the raw text from your browser into a text file on yourcomputer.
# You can use the count() method to find out how many times a word or phrase
# appears in a string. For example, the following code counts the number of
# times 'row' appears in a string:


# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3

# Notice that converting the string to lowercase using lower() catches all
# appearances of the word you’re looking for, regardless of how it’s formatted.
# Write a program that reads the files you found at Project Gutenberg and
# determines how many times the word 'the' appears in each text. This will be
# an approximation because it will also count words such as 'then' and 'there'.
# Try counting 'the ', with a space in the string, and see how much lower your
# count is.
print('\n---\n10-10\n---')
filenames = [
    'a_study_in_scarlet.txt', 'the_man_who_laughs.txt', 'scarlett_pimpernel.txt'
    ]

for filename in filenames:
    try:
        with open(filename) as f:
            content = f.read()
    except (FileNotFoundError, UnicodeDecodeError):
        print(f'We were unable to find and/or decode {filename}')
    else:
        count  = content.lower().count('the')
        print(f"{filename} features the word 'the' {count} times.")
