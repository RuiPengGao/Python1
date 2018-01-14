#Summing the digits in an integer
i = int(input("Integer between 0 to 1000= "))

#do the maths
a = i % 10
b = (i //10) % 10
c = (i // 100) % 10
d = (i //1000)
sum = a + b + c + d

# printing result
if 0 < i < 1000:
  print("Sum of digits in {0} is {1}".format(i,sum))
else:
  print("Error: number must be between 0 and 1000")
