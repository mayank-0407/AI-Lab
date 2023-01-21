def find_duplicates(dump,temp):
    data=[]
    a=[]
    b=[]
    if len(dump)>len(temp):
        a=dump.copy()
        b=temp.copy()
    else:
        a=temp.copy()
        b=dump.copy()
    length_a=len(a)
    length_b=len(b)
    for i in range(0,length_a):
        # print(a[i],b[i])
        for j in range(0,length_b):
            if a[i] == b[j]:
                data.append(a[i])
    print('Duplicates in Given lists are: ')
    print(data)

    return None


dump=[1,2,4,5,6]
temp=[1,8,5,9]
find_duplicates(dump,temp)