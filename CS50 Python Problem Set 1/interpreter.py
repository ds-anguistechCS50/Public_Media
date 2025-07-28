expression = input("What is your math problem? ")
if expression.count(' ') < 2:
    expression = expression.replace(" ", "")
    expression = ' '.join(expression)
    x, y, z = expression.split(" ")
else:
    x, y, z = expression.split(" ")

x = float(x)
z = float(z)

if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)
