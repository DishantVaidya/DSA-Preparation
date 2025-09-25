print("Seprate Chaining Technique")

h0=[]
h1=[]
h2=[]
h3=[]
h4=[]

n=int(input("Enter the number of keys:"))

print("Enter the elements:")
for i in range(n):
    key=int(input())
    rel_add=key%5

    if rel_add==0:
        h0.append(key)
    elif rel_add==1:
        h1.append(key)
    elif rel_add==2:
        h2.append(key)
    elif rel_add==3:
        h3.append(key)
    elif rel_add==4:
        h4.append(key)                

print("Hash Table")
print("Index\tKey")
print(h0)
print(h1)
print(h2)
print(h3)
print(h4)