def main():
# ask user what time it is
      meal_time = input("What time is it? ")
#call the convert function to process user input
      convert(meal_time)

# convert function takes user input
# splits it into two variables between the : and converts them into floats
# concatinates to get usable value for the if statement
# to determine what meal to print
def convert(meal_time):
    hours, minutes = meal_time.split(":")
    hours = float(hours)
    minutes = float(minutes) / 60
    conv_time = (hours + minutes)
    if conv_time >= 7.0 and conv_time <= 8.0:
       print("breakfast time")
    elif conv_time >= 12.0 and conv_time <= 13.0:
       print("lunch time")
    elif conv_time >= 18.0 and conv_time <= 19.0:
       print("dinner time")
    else:
      print("")
    return conv_time

if __name__ == "__main__":
      main()
