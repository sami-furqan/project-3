print("Enter three numbers to find the mean and the greatest amongst them")
print()
def getMean(a,b,c):
  mean= (a+b+c)/3
  print("mean is", mean)

def isGreater (a,b,c):
  if(a>b and a>c):
    print(a,"is greater")
  elif(b>a and b>c):
      print(b,"is greater")
  elif(a==b and b==c):
      print("All are equal")
  elif(a==b and a>c):
      print(a,"and",b,"are equal and greater") 
  elif(a==c and a>b):
      print(a,"and",c,"are equal and greater")
  elif(b==c and b>a):
      print(b,"and",c,"are equal and greater")
  else:
      print(c,"is greater")

a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
c= int(input("Enter third number: "))

getMean(a,b,c)
isGreater(a,b,c)