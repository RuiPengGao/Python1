num = int(input("Integer between 0 to 1000= "))
x  = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)
if 0 < num < 1000:
  print("Sum of digits in {0} is {1}".format(i,sum))
else:
  print("Error: number must be between 0 and 1000")
