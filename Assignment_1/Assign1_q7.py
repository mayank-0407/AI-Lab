import string
def checkpass():
    password= input('Enter Your Password(it must have 1 lower digit,1 upper digit,1 num,1 special digit): ')
    print(len(password))
    if len(password)<8:
        print('pass should have more than 8 digit')
        return None
    l,u,d,alpha = 0,0,0,0

    for i in password:
        if i.islower():
            l+=1
        if i.isupper():
            u+=1
        if i.isdigit():
            d+=1
        if i=='@' or i=='$' or i=='*' or i=='_':
            alpha+=1
    if l>=1 and u>=1 and d>=1 and alpha>=1:
        print('Password is valid and saved successfully')
    else:
        print('Invalid Password')


checkpass()
