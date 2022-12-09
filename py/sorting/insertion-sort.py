import math
def sort(arr):
    for i in range(1,len(arr)):
        j=i
        while j>=0 and arr[j-1] > arr[j]:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j-=1
    return arr
arr=[2,42,5,6,9,7]

print(sort(arr))

# a=int((3+4)/2)
# print(a)

