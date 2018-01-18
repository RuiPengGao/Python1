#converting fahrenheit to celsius

Fahrenheit = float(input("Enter Fahrenheit: "))

celsius = (5/9) * (Fahrenheit - 32)

print("{0}°F is converted to {1:1.1f}°C.".format(Fahrenheit,celsius))
