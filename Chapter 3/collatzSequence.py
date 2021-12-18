#Collatz sequence
def collatz(number):
    if number%2 == 0:
        number=number//2
        print(str(number))
        return number
    else:
        number=3*number+1
        print(str(number))
        return number

print("Enter number:")
while True:
    try:
        collatzNo=int(input())
        break
    except ValueError:
        print("Incorrect input. Must enter an integer.")

while collatzNo != 1:
    collatzNo=collatz(collatzNo)
    
