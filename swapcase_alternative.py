#ask the user to input words with improper casing
user_input = input("Please enter word/s with improper casing: ")
#use isupper and islower to check the casing
#use if statements to swap the cases
if user_input.isupper():
    user_input.lower()
elif user_input.islower():
    user_input.upper
#print the result