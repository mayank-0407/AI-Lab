# Given two jugs- a 4 litre and 3 litre capacity. Neither has any measurable markers on it. There
# is a pump which can be used to fill the jugs with water. Simulate the procedure in Python to get
# exactly 2 litre of water into 4-litre juga

# means tuples can be (4,0),(0,3),(4,3),(0,0)
# end is (2,'something')

def get_2l_in_4ljug():
    start=[0,0]
    a_cap=4
    b_cap=3
    print(start)
    while(start[0]!=2):
        if start[0]==0 and start[1]==0:
            start[1]=3
        elif start[0]==4:
            start[0]=0
            start[0]=start[1]
            start[1]=0
        elif start[1]==0:
            start[1]=3
        elif start[1]==b_cap and start[0]!=a_cap and start[1]!=0:
            temp=start[0]
            r_cap=a_cap-temp
            if r_cap>=start[1]:
                start[0]=start[0]+start[1]
                start[1]=0
            elif r_cap<start[1]:
                start[0]=4
                start[1]=start[1]-r_cap
        
        print(start)
print("Water Jug Problem starts in which output is [2,] :: ")
get_2l_in_4ljug()