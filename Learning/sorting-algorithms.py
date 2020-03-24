#bubble sort
def bubble_sort(A):
    n = len(A)
    for passnum in range(n):
        for i in range(n-1):
            if A[i] > A[i+1]:
                A[i+1],A[i] = A[i],A[i+1]
    return A

#merge sort
def mergeSort(arr):
    print("Splitting ",arr)
    if len(arr) > 1:
        mid = len(arr) //2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i=j=k=0

        while i < len(L) and j <len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        while i <len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j<len(R):
            arr[k] = R[j]
            j+=1
            k+=1
    print("Merging ",arr)
