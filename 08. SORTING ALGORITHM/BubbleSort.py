print("Bubble Sorting")

a = [4,2,3,1,5]
n=len(a)
print("Array =",a)

for p in range(n-1):
    print('Pass -',p+1)
    for i in range(n-p-1):
        if a[i]>a[i+1]:
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp
        print("Sorted array -",a)