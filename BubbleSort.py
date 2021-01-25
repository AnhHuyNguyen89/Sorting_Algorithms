#Bubble Sort
def bubbleSort(arr):
    a = len(arr)
    #Traverse or go through  all array elements by using loop
    for i in range(a):
        for j in range(0,a-i-1):
            #if the first number is greater than the second number, we will swap themselves
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j +1], arr[j]
arr = [66,61,12,13,0,9,45]
#calling method
bubbleSort(arr)
print("The sorted list is: ")
for i in range(len(arr)):
    print("%d" %arr[i])
"""
Bubble Sort check number and compare it to the larger number
If the first element is larger than the second element, we swap them
This process continues to the last pair of items in the list.
"""
    