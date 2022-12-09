
for i in range(7):
    for k in range(6-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for l in range(i+1):
        print("*",end="")
    print()
for i in range(6):
    for k in range(i+1,0,-1):
        print(" ",end="")
    for j in range(6, i, -1):
        print("*",end="")
    for l in range(6, i+1, -1):
        print("*",end="")
    print()

# print("*"*5)

