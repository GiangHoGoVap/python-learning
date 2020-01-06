#Python program to check if the number has perfect square root or not
import math
x = int(input("Enter a number to check square root: "))
root = math.sqrt(x)
if int(root+0.5)**2==x:
    print("This number has perfect square root ",root)
else:
    print("This number is not beautiful")
