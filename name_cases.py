# Save each of the following exercises as a separate file with a name like name_cases.py. If you get stuck, take a break or see the suggestions in Appendix C.

# 2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
person = 'alan'
message = f'Hello {person.title()}, would you like to learn some Python today?'
print(message)

# 2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.
print(person.lower())
print(person.upper())
print(person.title())

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:
### Albert Einstein once said, “A person who never made a mistake never tried anything new.” ###
famous_quote = f'{person.title()} Turing once said, “It is possible to invent a single machine which can be used to compute any computable sequence.”'
print(famous_quote)

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.
famous_person = 'alan turing'
famous_quote = f'{famous_person.title()} Turing once said, “It is possible to invent a single machine which can be used to compute any computable sequence.”'

# 2-7. Stripping Names: Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
person_with_whitespace = '\talan\nturing '
print(person_with_whitespace)
print(person_with_whitespace.rstrip())
print(person_with_whitespace.lstrip())
print(person_with_whitespace.strip())
