print("Searching an element")

a=[10,20,30,40,50,60]
print("array =",a)

n = len(a)
flag=0

data=int(input("Enter the element to be Searched :"))

for i in range(n):
    if a[i]==data:
        flag=1
        break

if flag==0:
    print("Element entered is Not Found in given array.")
else:
    print("Element entered is Found in given array.")