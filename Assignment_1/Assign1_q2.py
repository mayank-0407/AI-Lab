import random

def ShowRandomno():
    
    temp_arr=[]
    for i in range(0,101):
        temp_arr.append(random.randint(100,900))
        
    return temp_arr
def ShowOddNumber(temp_list):
    
    temp_oddno=[]
    temp_evenno=[]
    for i in range(0,100):
        if temp_list[i]%2==0:
            temp_evenno.append(temp_list[i])
        elif temp_list[i]%2==1:
            temp_oddno.append(temp_list[i])               
    print('Odd Number are:- '+ str(temp_oddno))
    print('Even Number are:- '+ str(temp_evenno))
    
def ShowPrimeNumber(temp_list):
    
    temp_primeno=[]
    flag=0
    for j in range(0,100):
        for i in range(2, int(temp_list[j]/2)+1):
            if (temp_list[j] % i) == 0:
                break
            else:
                flag=1
        if flag==1:        
            temp_primeno.append(temp_list[j])
            flag=0
    print('Prime Number are:- '+ str(temp_primeno))
    
temp_list=ShowRandomno()
print('Here is list of Random Numbers: ')
print(temp_list)
ShowOddNumber(temp_list)
ShowPrimeNumber(temp_list)