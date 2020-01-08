#Python program to check arithmetic progression or not
def Arithmetic(x):
    delta = x[1] - x[0]
    for i in range (len(x)-1):
        if not (x[i+1] - x[i] == delta):
            return False
    return True

sequence=[]
number=int(input("Enter sequence length: "))
print("Enter numbers")
for i in range(number):
    data=int(input())
    sequence.append(data)

print(Arithmetic(sequence))