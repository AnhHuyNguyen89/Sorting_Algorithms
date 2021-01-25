# Selection Sort
import sys
A = [0, 15, 98, 78, 1, 24, 6]
for i in range(len(A)):
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]
print("Sorted Array: ")
for i in range(len(A)):
    print("%d" % A[i])

"""
Selection Sort that we need to find the smallest number in the array after that compared 
and change with the second number until the last item of the list is 
the remaining element to be examined.
"""
