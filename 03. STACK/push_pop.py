s=[0,0,0,0,0]
max_n=4
top=-1
ans=1

def push():
    global s
    global top
    if top==max_n:
        print("Stack OVerflow")
    else:
        data=int(input("Enter the element"))
        top=top+1
        s[top]=data

        print("Stack")
        for i in range(top+1):
            print(s[i],end=" ")   

def pop():
    global s
    global top
    if top==max_n:
        print("Stack OVerflow")
    else:
        data=s[top]
        print(data,"is removed")
        top=top-1
        print("stack")
        for i in range(top+1):
            print(s[i],end=" ")

while(ans!=3):
    ans=int(input("Enter your choice\n1.push\n2.pop\n3.exit\n"))
    if ans==1:
        push()
    elif ans==2:
        pop()
    elif ans==3:
        print("O.K")
    else:
        print("Invalid")
        ans=0    