#converting fahrenheit to celsius

Fahrenheit = float(input("Enter Fahrenheit: "))

celsius = (5/9) * (fahrenheit - 32)

print("{0}°F is converted to {1:1.1f}°C.".format(fahrenheit,celsius))
