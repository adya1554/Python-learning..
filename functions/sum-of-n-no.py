def sum(n):
    if n==1:
        return 
    return sum(n-1) + 1

n = int(input("enter no : "))
print(sum(n))