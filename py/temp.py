# list = [ [1,32,4,1,4,], 
# [2,4,1,5,2,3],
# [4,78,4,8,9,23,5] ]

# def printarr(arr):
#     for i in arr:
#         for j in i:
#             print(j,end=" ")
#         print()


# m = int(input("enter rows"))
# n = int(input("enter colums"))
# list = []
# for i in range(m):
#     temp = []
#     for j in range(n):
#         temp.append(int(input("enter values")))
#     list.append(temp)

        

# printarr(list)

# mapp = {}     

# for i in range(6,1,-1):
#     print(i)

# print(int(-3/2))

# print(-10%3)

# import math
# print(math.fmod(10,3))

# print(float("inf"))

# a,b = [1,3]
# print(a, b)

# arr = [i for i in range(4)]
# print(arr)

# arr1 = [[2]*3 for i in range(4)]
# print(arr1)

# arr = [[0]* 3 for i in range(4) ] 
# print(arr)


def majorityElement(nums):
        map = {}
        for i in nums:
            if i in map:
                map[i] = map[i]+1
            else:
                map[i] = 1
                
        maxi = 0
        for key,value in map.items():
            if value > len(nums) // 2:
                maxi = key
        return maxi
ans = [2,2,1,1,1,2,2]
print(majorityElement(ans))