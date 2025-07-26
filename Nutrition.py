# CS50 with Python - Problem Set 2

values = {'Apple' : 130,
'Avocado' : 50,
'Banana' : 110,
'Cantaloupe' : 50,
'Grapefruit' : 60,
'Grapes' : 90,
'Honeydew Melon' : 50,
'Kiwifruit' : 90,
'Lemon' : 15,
'Lime' : 20,
'Nectarine' : 60,
'Orange' : 80,
'Peach' : 60,
'Pear' : 100,
'Pineapple' : 50,
'Plums' : 70,
'Strawberries' : 50,
'Sweet Cherries' : 100,
'Tangerine' : 50,
'Watermelon' : 80
}

# Ask user for input
# Format to title case to match dictionary keys
fruit = input("Item? ").title()

# If input doesn't have a match in the dictionary, return nothing
# otherwise return the calorie count
if fruit not in values:
    print("")
else:
    print("Calories: ", values[fruit])
