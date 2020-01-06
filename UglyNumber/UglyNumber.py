#Python program to check if the number is ugly number or not
def Ugly(num):
        if num == 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        return num == 1

x=int(input("Enter a number: "))
print(Ugly(x))
