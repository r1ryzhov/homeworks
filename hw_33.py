# Level 1

def area(a, b, c):
    p = (a+b+c)/2
    area = (p*(p-a)*(p-b)*(p-c)) ** 0.5 # or from math import sqrt
    return area