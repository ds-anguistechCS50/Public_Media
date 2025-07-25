# CS50 for Python Problem Set 2

# characters that are not allowed in the vanity plate
puncuation = (".,?! ")

# initialize the criteria checkoff variable
final_answer = []

# request user input
# receive return regarding input meeting criteria 
# outputing input validation according to criteria 
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Function to vaildate user input according to the following criteria:
#
# All vanity plates must start with at least two letters.
# vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
# Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.
# No periods, spaces, or punctuation marks are allowed.
#
# user input is validated in each step and the boolian response is collected in the variable final_answer
def is_valid(plate):
    final_answer.append(plate[:2].isalpha())
    final_answer.append(len(plate) <= 6)
    for marks in plate:
        if marks in puncuation:
            final_answer.append(False)
    else:
        final_answer.append(True)
    final_answer.append(plate[1:-2].isalpha())
    for quest in plate:
        if quest.isdigit():
            if int(quest)==0:
                final_answer.append(False)
            else:
                break
# returns the final answer True or False to the main function
  return all(final_answer)

main()

