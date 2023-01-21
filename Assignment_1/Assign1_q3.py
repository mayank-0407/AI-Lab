def ShowPrimeNumber(num1,num2):
    
    temp_primeno=[]
    flag=0
    for j in range(num1,num2+1):
        if j==2:
            temp_primeno.append(j)
        if j==3:
            temp_primeno.append(j)
        for i in range(2, int(j/2)+1):
            if (j % i) == 0:
                break
            else:
                flag=1
        if flag==1:        
            temp_primeno.append(j)
            flag=0
            
    print('Prime Number are:- '+ str(temp_primeno))

ShowPrimeNumber(2,9)