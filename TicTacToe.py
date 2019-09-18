a=['1','2','3','4','5','6','7','8','9']
def disp():
    z=0
    for i in range(0,3):
        for j in range(0,3):
            print (a[z],end=' ')
            z=z+1
        print()

def check():
    if(a[0]=='x'):
        if(a[1]=='x'and a[2]=='x'):
            return 1
        if(a[3]=='x'and a[6]=='x'):
            return 1
    if(a[4]=='x'):
        if(a[1]=='x'and a[7]=='x'):
            return 1
        if(a[3]=='x'and a[5]=='x'):
            return 1
    if(a[8]=='x'):
        if(a[6]=='x'and a[7]=='x'):
            return 1
        if(a[2]=='x'and a[5]=='x'):
            return 1
    if(a[0]=='x'and a[4]=='x'and a[8]=='x'):
        return 1
    if(a[2]=='x'and a[4]=='x'and a[6]=='x'):
        return 1
    if(a[0]=='o'):
        if(a[1]=='o'and a[2]=='o'):
            return 2
        if(a[3]=='o'and a[6]=='o'):
            return 2
    if(a[4]=='o'):
        if(a[1]=='o'and a[7]=='o'):
            return 2
        if(a[3]=='o'and a[5]=='o'):
            return 2
    if(a[8]=='o'):
        if(a[6]=='o'and a[7]=='o'):
            return 2
        if(a[2]=='o'and a[5]=='o'):
            return 2
    if(a[0]=='o'and a[4]=='o'and a[8]=='o'):
        return 2
    if(a[2]=='o'and a[4]=='o'and a[6]=='o'):
        return 2
    return 0
    
print("\t\tGAME START")
disp()
x=0
f=0
while(x<9 and f==0):
    while True:
        print("Player",(x%2)+1," :",end=' ')
        y=int(input())
        if(a[y-1]!='x' and a[y-1]!='o'):
            break
    if(x%2==0):    
        a[y-1]='x'
    else:
        a[y-1]='o'
    disp()
    f=check()
    x=x+1
if(f==0):
    print("\n\tMatch Draw")
elif(f==1):
    print("\n\tPlayer 1 WINS !!!")
elif(f==2):
    print("\n\tPlayer 2 WINS !!!")
x= input();
