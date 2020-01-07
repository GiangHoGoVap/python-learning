#Python program to calculate the arc length of an angle
def ArcLength(diameter,degree):
  pi=22/7
  rad = float(degree*pi/180)
  radius = int(diameter/2)
  s = abs(float(radius*rad))
  return s
  
diameter=int(input("Enter the diameter: "))
degree=int(input("Enter the angle measure: "))
print("The arc length is: ",ArcLength(diameter,degree))
