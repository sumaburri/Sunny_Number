number=int(input('Enter a Nummber : '))
n=1
while((n**2)<=number+1):
    if (n**2)==number+1:
        print('Sunny Number')
        break
    n=n+1
else:
    print('Not a Sunny Number')
    
