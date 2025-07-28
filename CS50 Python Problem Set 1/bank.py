# Get greeting from user
# And covert to lower case and remove any extra spaces

say_hi = input("Greetings! ").lower().strip()

# If greeting begins with hello, print $0 to screen
# If greeting begins with an H, but is not hello, $20 printed to screen
# Otherwise, $100 printed to screen

if say_hi.startswith("hello"):
       print("$0")
elif say_hi.startswith("h") and say_hi != "hello":
      print("$20")
else:
      print("$100")
