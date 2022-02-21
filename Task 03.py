# Python program to find remainder
# without using modulo operator




dividend = float(input("Enter dividend : "))

divisor = float(input("Enter divisor : "))

quo = 0

while True:
    
    dividend -= divisor
    quo +=1
    if(dividend < divisor):
        break

print(quo)
print(dividend)
