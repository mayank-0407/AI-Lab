def find_leapyear():
    left=int(input('Enter 1st limit:-'))
    right=int(input('Enter 2nd limit:-'))

    if left>right:
        temp=right
        right=left
        left=temp
    print('Leap Years in given range are: ')
    leap_year=[]
    while left<right:
        if left%4==0 and left%100!=0:
            leap_year.append(left)
        if left%100==0 and left%400==0:
            leap_year.append(left)

        left=left+1
    print(leap_year)
find_leapyear()
    