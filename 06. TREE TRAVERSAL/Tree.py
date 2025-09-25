print("Tree Traversal")

def pre_order(root):
    if t[root]=='-':
        return
    else:
        print(t[root],end=" ")

    left=(2*root)+1
    right=(2*root)+2

    if left<n:
        if t[left]!='-':
            pre_order(left)
        
    if right<n:
        if t[right]!='-':
            pre_order(right)  
           
    return

def in_order(root):
    if t[root]=='-':
        return
        
    else:
        print(t[root],end=" ")

    left=(2*root)+1
    right=(2*root)+2

    if left<n:
        if t[left]!='-':
            in_order(left)

    print(t[root],end=" ")    

    if right<n:
        if t[right]!='-':
            in_order(right)  
    return

def post_order(root):    
    if t[root]=='-':
        return
        
    left=(2*root)+1
    right=(2*root)+2

    if left<n:
        if t[left]!='-':
            post_order(left)       

    if right<n:
        if t[right]!='-':
            post_order(right)  

    print(t[root],end=" ")       
    return  

#Main program
h=int(input("Enter height of the tree:"))
n=(2**(h+1))-1
print("Number of nodes:",n)
t=[]

print("Enter array:")
for i in range(n):
    print(i,".",end=" ")
    x=input()
    t.append(x)

print("Parent\tLeft\tRight")
for i in range(n//2):
    print(i,".",end=" ")
    print(t[i],"\t",t[(2*i)+1],"\t",t[(2*i)+2])
    print()

print("Pre-Order Traversal=",end="")
pre_order(0)
print("In-Order Traversal=",end="")
in_order(0)
print("Post-Order Traversal=",end="")
post_order(0)
      
