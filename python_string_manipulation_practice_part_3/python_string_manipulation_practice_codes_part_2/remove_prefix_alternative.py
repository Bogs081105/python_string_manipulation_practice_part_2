#set a sample string
string = ("Pogi Kyrie")
#set a prefix
prefix = ("Pogi")
#check if the word has a prefix that has been set
if string.startswith(prefix):
#remove the prefix
    string = string.replace(prefix, "", 1)
#print the result
print(string)