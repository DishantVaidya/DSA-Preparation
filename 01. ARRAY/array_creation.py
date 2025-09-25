print("Creating an array")

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