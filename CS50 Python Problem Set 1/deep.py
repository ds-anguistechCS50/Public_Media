# Ask user to input an answer to the question
# What ever answer is input is converted to all lower case
# and stripped of all leading and ending spaces

answer = input("What is answer to the Great Question of Life, " \
"the Universe and Everything? ").lower().strip()

# If any of the three listed cases is input, then Yes is printed to screen
# If not, No is printed to the screen

match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
