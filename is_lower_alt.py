#ask the user to input a word/words
string = input("Please enter a word: ")
#check all the characters in the input
for char in string:
#convert characters to its unicode value using ord
#using ASCII, check if the character is within the letters a - z in their unicode values
    (97 <= ord(char) <= 122 for char in string if char.isalpha())
#check if all the values are true
#print if it is lower