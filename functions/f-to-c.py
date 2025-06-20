# profram for converting farnhite to celcius-----------------

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("enter farenhit temprature : "))
a = f_to_c(f)
print(round(a, 1))