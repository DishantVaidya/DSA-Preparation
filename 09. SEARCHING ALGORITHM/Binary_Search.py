print("Binary Search")

a=[10,20,25,51,75,200,250,500]
print("Array -",a)

n = len(a)
flag=0

data = int(input("Element to ssearch:"))

start=0
end=n-1
print("Start\tEnd\tMid")
while start<=end:
    mid = int((start+end)/2)
    print(start,"\t",end,"\t",mid)

    if data==a[mid]:
        flag=1
        break
    elif data<a[mid]:
        end=mid-1
    else:
        start=mid+1

if flag==0:
    print("Element entered is Not Found in given array.")
else:
    print("Element entered is Found in given array at position :",mid)
