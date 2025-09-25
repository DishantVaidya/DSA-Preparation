print("Inserting an element")

a=[]
arr_size=int(input("Enter the size of an array:"))

for i in range(arr_size):
    a.append(0)

n=int(input("Enter the total elemnts:"))

for i in range(n):
    a[i]=int(input())

print("Array :",end=" ")
for i in range(n):
    print(a[i],end=" ")

new = int(input("\nEnter the new element :"))
k = int(input("Enter the position:"))

i = n - 1

while i>=k-1:
    a[i+1]=a[i]
    i=i-1

a[k-1]=new
n=n+1

print("Array :",end=" ")
for i in range(n):
    print(a[i],end= " ")
