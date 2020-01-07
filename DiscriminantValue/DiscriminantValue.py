#Python program to calculate the discriminant value
def Discriminant(x,y,z):
  delta = int (y**2 - 4*x*z)
  print("Discriminant value: ",delta)
  if delta > 0:
    print ("Two Solutions")
  elif delta == 0:
    print ("Only 1 solution")
  else:
    print ("No solution")
    
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
print(a,"x^2 + ",b,"x + ",c,"=0")
Discriminant(a,b,c)
