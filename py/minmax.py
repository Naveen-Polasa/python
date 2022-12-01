n = int(input())
for i in range(n):
    def maxArr(arr):
        maxi = []
        for i in range(len(arr)):
            maxi.append(maximum(0,i+1,arr))
        return maxi

    def maximum(st,en,arr):
        maxi = 0
        for st in range(en):
            if arr[st] > 0:
                maxi+=arr[st]
        return maxi

    def minimum(st,en,arr):
        mini = 0
        for st in range(en):
            if arr[st] < 0:
                mini+=arr[st]
        return mini 

    def minArr(arr):
        mini = []
        for i in range(len(arr)):
            mini.append(minimum(0,i+1,arr))
        return mini

    lst = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        ele = int(input())
        lst.append(ele) 

    maxi = maxArr(lst)
    mini = minArr(lst)
    for i in range(len(lst)):
        lst[i] = maxi[i]+mini[i]
    print(lst)




#     t=int(input())

# for e in range(t):
#     n= int(input())

#     l = list(map(int(input())))[:n]

#     for i in range(n):
#         for j in range(i+1,n+1):
#             l2 = l[:i+1]
#             sl = sum(l2)
#             print(sl,end=" ")
#     print()