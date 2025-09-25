queue = []

def INSERT(elt):
    queue.append(elt)
    print(elt, "inserted")

def DELETE():
    if queue:
        elt = queue.pop(0)
        print(elt, "deleted")
    else:
        print("Queue is empty, nothing to delete")

def DISPLAY():
    print("Queue :", queue)      

ch=1

while ch>0 and ch<4:
    print("1.INSERT\n2.DELETE\n3.DISPLAY\n4.EXIT")
    ch=int(input("Enter your choice: "))
    if ch==1:
        elt=int(input("Enter element to be inserted: "))
        INSERT(elt)
    elif ch==2:
        DELETE()
    elif ch==3:
        DISPLAY()
    else:
        break