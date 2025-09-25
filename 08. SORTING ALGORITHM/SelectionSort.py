print("Selection Sorting")

A = [4,7,12,5,24,83]
print("Array =",A)

n = len(A)

for i in range(n-1):
    min_elt=A[i]
    flag=0
    for j in range(i+1,n):
        if min_elt>A[j]:
            min_elt=A[j]
            pos = j
            flag = 1
    if flag==1:
        temp=A[i]
        A[i]=A[pos]    
        A[pos]=temp
    print("Pass-",i+1)
    print("Sorted Array =",A)        