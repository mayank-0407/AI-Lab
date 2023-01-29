# Given three jugs: 12, 8 and 5 liter capacities. Largest jug is completely filled. Using these 3 jugs,
# split the water to obtain exactly 6 liter in largest jugs.

# start[12,0,0]  a=12,b=8,c=5
# ans[6, , ]
# steps are [4,8,0],[4,3,5],[9,3,0],[1,8,3],[1,6,5],[6,6,0]

def get_6l_in_12ljug():
    start=[12,0,0]
    a=12
    b=8
    c=5
    if start[0]+start[1]+start[2]==12:
        pass
    else:
        print("Sum of this problem is not 12")
    while(start[0]!=6):
        if start[1]==0:
            if start[0]<=b:
                start[1]=start[0]
                start[0]=0
            elif start[0]>b:
                rem=b-start[1]
                start[1]=b
                start[0]=start[0]-rem
        elif start[2]==0:
            if start[1]>=c:
                start[2]=c
                start[1]=start[1]-c
            elif start[1]<c:
                start[2]=start[1]
                start[1]=0
        elif start[2]==c:   # c is full
            start[0]=start[0]+start[2]
            start[2]=0
        elif start[2]<c and start[1]==b:
            rem=c-start[2]
            start[2]=c
            start[1]=start[1]-rem
        print(start)
print("Water Jug Problem starts in which output is [2, , ] :: ")
get_6l_in_12ljug()