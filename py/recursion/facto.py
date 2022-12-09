
def rec(n):
    if n == 0:
        return 1
    return n*rec(n-1)
    

ans = rec(int(input("enter the number")))
print(ans)