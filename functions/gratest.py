def gratest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a=10
b=12
c=14
print(f"The gratest amung three numbers is {gratest(a, b, c)}")