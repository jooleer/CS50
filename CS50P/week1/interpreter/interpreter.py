expression = input("Expression: ")
x, y, z = expression.split(" ")

x = int(x)
z = int(z)

match y:
    case "+":
        result = x + z
    case "/":
        result = x / z
    case "*":
        result = x * z
    case "-":
        result = x - z

result = float(result)
print(round(result, 1))
