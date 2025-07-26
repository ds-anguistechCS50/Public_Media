# ask user for their variable name
variable_name = input("variableName? ")

# iterate through characters of user input
# if the character is upper case print an underscore
# and the lower case of the character with no line feed
# if the character is lower case, just print the character with no line feed
for c in variable_name:
    if c.isupper() == True:
        print("_" + c.lower(), end="")
    elif c.isupper() == False:
        print(c, end="")
# print a blank line
print()
