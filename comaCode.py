#Comma code

spam=['It is certain',
'It is decidedly so',
'Yes definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful']

def comaCode(someList):
    itemizedString=''
    i=0
    for item in someList:
        
        if i < len(someList)-2:
            itemizedString=itemizedString + str(item) + ', '
        elif i == len(someList)-2:
            itemizedString=itemizedString + str(item) + ' and '
        else:
            itemizedString=itemizedString + str(item)
        i+=1
        
    print(itemizedString)

comaCode(spam)
