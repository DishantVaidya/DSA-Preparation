print("insertion sort")

a=[5,-1,2,7,3]
print("Array =",a)
n=len(a)

for i in range(1,n):
    temp=a[i]
    k = i-1

    while temp<a[k] and k>-1:
        a[k+1]=a[k]
        k = k-1
    a[k+1]=temp
    print("Pass -",i)
    print("Sorted Array =",a)   

    