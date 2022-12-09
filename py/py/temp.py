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


# def majorityElement(nums):
#         map = {}
#         for i in nums:
#             if i in map:
#                 map[i] = map[i]+1
#             else:
#                 map[i] = 1
                
#         maxi = 0
#         for key,value in map.items():
#             if value > len(nums) // 2:
#                 maxi = key
#         return maxi
# ans = [2,2,1,1,1,2,2]
# print(majorityElement(ans))

# def isPalindrome(s):
#         s = s.lower()
#         ss = ""
#         for i in s:
#             if i >= 'a' and i <= 'z':
#                 ss+=i
        
#         print(ss)
#         st, en = 0, len(ss)-1
#         while st <= en:
#             if ss[st] != ss[en]:
#                 return False
#             st+=1 
#             en-=1
#         return True

# print(isPalindrome("0P"))

# s = "naveen"

# print(s[::-2])

# arr = [2, 3, 6, 6, 55,24,6,2,1,5,12,6,64,63,3,23,111]
# maxi = float('-inf')
# sMaxi = float('-inf')

# for i in arr:
#     maxi = max(i,maxi)

# for j in arr:
#     if j < maxi:
#         sMaxi = max(j,sMaxi)

# print(sMaxi)
# tup2 = 'gh','yugy'
# tup1 = (1)
# tup = tuple('1')
# print(type(tup2))

# mapp = {1:'naveen',2:'developer'}
# print(mapp[2])

# print(not False)
# a=20
# b=20
# print(id(a))
# print(id(b))

# print(a==b)
# print(a is b)

# a=range(123,1213)

# print(a)

# def number(num):
#     """this is docstring"""
#     print(num)

# print(number.__doc__)

# x=21
# x1 =  lambda x : x*x*x
# print(x1(7))

# tables = [lambda x: x*x for x in range(1,11)]
# print(tables)

# for i in tables:
#     print(i)

# l = [x+1 for x in range(21)]

# print(l)

# a = "naveen polasa"
# b = a[::-1]
# print(b)

# print(a[7:10:2])

# Python Program to Update
# character of a String

# String1 = "Hello, I'm a Geek"
# print("Initial String: ")
# print(String1)

# Updating a character of the String
## As python strings are immutable, they don't support item updation directly
### there are following two ways
#1
# list1 = list(String1)
# list1[2] = 'p'
# String2 = ''.join(list1)
# print("\nUpdating character at 2nd Index: ")
# print(String2)

#2
# String3 = String1[0:2] + 'p' + String1[3:]
# print(String3)

# a = "this is string"
# b = "this is also a string"
# print(a+b)

# print(repr("hello \n there"))

# def merge(nums1, m, nums2, n):
#         ans = []
#         c1,c2 = 0, 0
#         i=0
#         while c1 < m and c2 < n:
#             if nums1[c1] < nums2[c2]:
#                 ans.append(nums1[c1])
#                 c1+=1
#             elif nums1[c1] >= nums2[c2]:
#                 ans.append(nums2[c2])
#                 c2+=1

#         while c1 < m:
#             ans.append(nums1[c1])
#             c1+=1

#         while c2 < n:
#             ans.append(nums2[c2])
#             c2+=1

#         for i in range(len(nums1)):
#             nums1[i] = ans[i]
#         return nums1

# nums1 = [1,2,3,0,0,0]
# m = 3

# nums2 = [2,5,6]
# n = 3
# merge(nums1,m, nums2,n)
# print(nums1)
# print(merge([2,0],2,[1],1))


# li = [1,43,5,245,24,12,4,5,23,42]
# li=['hey','hello','how','are','you']
# l1 = sorted(li, key=len)
# li.sort(key=len)
# print(li)

# lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
# lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

# lst3 = [val for val in lst1 if val in lst2]
# print(lst3)

# tuple1 = (1, 4, 5, 1)
# print(type(tuple1))

# for i in range(5):
#     num = 1
#     for j in range(5-i, 0 ,-1):
#         print(num, end='')
#         num+=1
#     print()