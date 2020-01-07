#Python program to print the distance between 2 points
import math

x1=int(input("Enter x1: "))
y1=int(input("Enter y1: "))
print("The first point is (",x1,",",y1,")")

x2=int(input("Enter x2: "))
y2=int(input("Enter y2: "))
print("The second point is (",x2,",",y2,")")

D=float((x1-x2)**2+(y1-y2)**2)

print("The distance between two point is: ",math.sqrt(D))
