import math

def setDomain(a,b,c):
    domain = b - a
    width = domain/c
    return width

def nonintegrableFunction(a,b):
    #Function is set below
    func = math.sin(a**2)+1
    area = func*b
    absArea = abs(area)
    return absArea

def minimumArea(a,b,c):
    area = 0
    while True:
        if a >= b:
            break

        area += nonintegrableFunction(a,c)
        a+=c

    return area

def maximumArea(a,b,c):
    area = 0
    while True:
        a+=c
        area += nonintegrableFunction(a,c)

        if a >= b:
            break

    return area

def riemannSum(a,b):
    average = (a+b)/2
    return average

min = int(input("Minimum X: "))
max = int(input("Maximum X: "))
sec = int(input("Number of Sections: "))

width = setDomain(min,max,sec)
minArea = minimumArea(min,max,width)
maxArea = maximumArea(min,max,width)
accArea = riemannSum(minArea,maxArea)

print("\n\nLower Sum:",minArea)
print("Upper Sum:",maxArea)
print("\n\nArea:",accArea)
