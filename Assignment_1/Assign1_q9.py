def do_que9():
    D= {1:"One", 2:"Two", 3:"Three", 4: "Four", 5: "Five"}
    count=0
    # (i) WAP to add new entry in D; key=6 and value is “Six”
    D[6]='Six'
    print('Added key=6 and value is “Six” Dictionary: ')
    print(D)
    # (ii) WAP to remove key=2.
    D.pop(2)
    print('Removed key=2 from Dictionary: ')
    print(D)
    # (iii) WAP to check if 6 key is present in D.
    print('Value of Key 6 Dictionary: ')
    print(D[6])
    # (iv) WAP to count the number of elements present in D.
    for i in range(0,len(D)):
        count+=1
    print('Count of Dictionary Elements: ')
    print(count)
    # (v) WAP to add all the values present in D.
    value=list(D.values())
    allvalues=''
    for i in range(0,len(value)):        
        allvalues= allvalues + value[i]
    print('Sum of all Values in Dictionay: ')
    print(allvalues)
do_que9()