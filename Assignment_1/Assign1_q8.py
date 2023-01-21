def do_que8():
    l=[10, 20, 30, 40, 50, 60, 70, 80]
    # (i) WAP to add 200 and 300 to L.
    l.append(200)
    l.append(300)
    print('Appending 200 and 300 in given list: ')
    print(l)
    # (ii) WAP to remove 10 and 30 from L.
    l.remove(10)
    l.remove(30)
    print('Removing 10 and 30 in given list: ')
    print(l)
    # (iii) WAP to sort L in ascending order.
    l.sort()
    print('Sorted Order of given list: ')
    print(l)
    # (iv) WAP to sort L in descending order.
    l.reverse()
    print('Descending Order of given list: ')
    print(l)
do_que8()