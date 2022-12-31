"""module to learn about exceptions"""

# throwsa ZeroDivisionError, and causes system to do traceback
# print(5/0)

#using try-except blocks
#prints what is in the except block if systems throws ZeroDivisionError
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")

#using exceptions to prevent crashes
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    #using try-except block for error resistance with else statement
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else: 
        print(answer)