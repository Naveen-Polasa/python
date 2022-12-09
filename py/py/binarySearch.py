def search(arr, t):
    i=0
    j=len(arr)-1
    while i <= j:
        mid = int(i + (j-i)/2)
        if arr[mid] == t:
            return mid
        elif arr[mid] < t:
            i = mid + 1
        else:
            j = mid - 1
    
    return -1

# num = [1,2,4,24,5,21]
# #num.reverse()
# print(num)
# print(search(num, 4))

# num = [i+i for i in range(5)]
# print(num)


# arr = [[0] * 4 for i in range(5)]
# # arr = [[0] * 4] * 5  

# print(arr)
# arr[2][1] = 3
# print(arr)

# print(ord('N'))

# sett = set()

# sett.add(13)
# sett.add(132)

# print(sett)

# mapp = {}
# mapp['navee'] = 23
# mapp['ramesh'] = 44

# print(mapp)

# print(mapp.keys())
# print(mapp.values())