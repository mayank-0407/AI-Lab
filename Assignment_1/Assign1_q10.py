def calculate_compundinterest():
    principal=int(input('ENter the principal amount(rs): '))
    Interest=float(input('ENter the Interest Rate(decimal): '))
    time=int(input('ENter the time(years): '))
    
    compund=principal*pow((1+Interest/100),time)-principal
    print('Compound Interest of Entered Values : ')
    print(compund)