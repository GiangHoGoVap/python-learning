#Python program to print duplicates from a list of integers
def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated

list1=[]
number=int(input("Enter list length: "))
print("Enter numbers")
for i in range(number):
    data=int(input())
    list1.append(data)

print("The number duplicates: ",Repeat(list1))
