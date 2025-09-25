print("Deleting an element")

a=[]
arr_size=int(input("Enter the size of an array:"))

for i in range(arr_size):
    a.append(0)

n=int(input("Enter the total elemnts:"))

for i in range(n):
    a[i]=int(input())

print("Array :",end=" ")
for i in range(n):
    print(a[i],end= " ")

k = int(input("\nEnter the position:"))  

i = k-1

while i<n-1:
    a[i]=a[i+1]
    i = i+1

n = n -1 

print("Array :",end=" ")
for i in range(n):
    print(a[i],end= " ")