#Python program to reverse bits of a number
def reverse_Bits(n):
        result = 0
        for i in range(32):
            result <<= 1
            result |= n & 1
            n >>= 1
        return result
            
x=int(input("Enter a decimal number: "))
print(reverse_Bits(x))
