import re

def f1(a,b,c):
    re = a+b+c
    r = f2(5, 4, 6)
    print(r)
    return [re,re+1,a,'t']

def f2(a,b,c):
    re = a+b+c
    return [re,re+1,a,'t']

r = f1(5,4,6)
r.append(9)
print(r)