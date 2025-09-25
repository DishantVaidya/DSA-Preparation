print("Linear Search")

A=[10,20,30,40,50,60]
print("Array = ",A)

n = len(A)
flag=0

data = int(input("Enter the number to be searched:"))

for i in range(n):
    if A[i]==data:
        flag=1
        break

if flag==0:
    print("Element entered is Not Found in given array.")
else:
    print("Element entered is Found in given array at position :",i)