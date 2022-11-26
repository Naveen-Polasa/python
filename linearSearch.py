def search(num,n):
    for i in range(len(num)):
        if(num[i] == n):
            return i


arr = [1,23,2,51,21,53]

print(search(arr,21))