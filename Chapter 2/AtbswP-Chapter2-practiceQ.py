##Practice questions

#Number 9
print('Please give me a number')
spam=input()
while True:
    try:
        int(spam)
    except ValueError:
        print('Error: Invalid input')
        break
        
    if int(spam)==1:
        print('Hello')
        break
    elif int(spam)==2:
        print('Howdy')
        break
    else:
        print('Greetings!')
        break


for i in range(1,11):
    print(i)
b=1;
while b <=10:
    print(b)
    b=b+1

