#Python program to check if the number x is power of y 
def isPower(n1,n2):
    if (n1==0):
        return False
    while (n1!=1):
        if (n1%n2 != 0):
            return False
        n1 = n1//n2
    return True

x=int(input("Enter a number: "))
y=int(input("Enter the number of power: "))
if(isPower(x,y)):
    print("This number is power of ",y)
else:
    print("This number is not")
