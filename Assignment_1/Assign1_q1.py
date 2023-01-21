def factorial(n):
    if n==0:
        return 1
     
    return n*factorial(n-1)
  
    
def find_sum(x,n):
    total=1
    for i in range(1,n+1):
        total=total+(pow(x,i)/factorial(n))
        return total
    
x=int(input("Input Value of X: "))
n=int(input("Enter value of n: "))
print('The sum of the series (1 + x + x2/2! + . . . + xn/n!):- ')
print(round(find_sum(x,n),2))