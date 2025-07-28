def main():
       feelings = input("How are you feeling? ")
       print(convert(feelings))

def convert(feelings):
       if ":(" in feelings and ":)" in feelings:
             return feelings.replace(":(", "\U0001F641").replace(":)", "\U0001F642")
       elif ":(" in feelings:
             return feelings.replace(":(", "\U0001F641")
       elif ":)" in feelings:
            return feelings.replace(":)", "\U0001F642")
       else:
            return(feelings)

main()
