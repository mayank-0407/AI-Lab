def calc(salary,temp):
    return (salary//100)*temp

def find_grossalary():
    b_salary=int(input('Enter Basic salary (rs):- '))

    if b_salary <= 10000:
        hra=20
        da=80
    elif b_salary<=20000:
        hra=25
        da=90
    elif b_salary>20000:
        hra=30
        da=95
    gross_salary=calc(b_salary,hra)+calc(b_salary,da)+b_salary
    print(gross_salary)
find_grossalary()