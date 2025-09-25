print("Hash Table")

h=[]
m=int(input("Enter the size of table :"))
n=int(input("Enter number of keys:"))

for i in range(m):
    h.append(0)

print("Enter the elements:")
for i in range(n):
    key=int(input())
    rel_add=key%m
    if h[rel_add]==0:
        h[rel_add]=key
        print("Relative Address=",rel_add)
    else:
        print("Relative Address=",rel_add,"Collision case")
print("Hash Table")
print("Index\tKey")
for i in range(m):
    print(i,"\t",h[i])