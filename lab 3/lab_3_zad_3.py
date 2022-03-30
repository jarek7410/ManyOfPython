import math
from math import sqrt
from random import random


def isCircle(x, y, r, tryX, tryY):
    return r >= sqrt(abs((tryX - r) * (tryX - r) + (tryY - r) * (tryY - r)))

def isSin(x,y,r,tryx,tryy):
    return math.sin(tryx*2)>=tryy


def monteCarlo(number, warunek):
    inside = 0
    for i in range(number):
        # if(isCircle(1,1,0.5,random(),random())):
        if (warunek(1, 1, 0.5, random(), random())):
            inside += 1
    return inside;


number = 1000000
inside = monteCarlo(number, isCircle)
pole = (inside / number)

print("kolo")
print("licząc metodą monte carlo: ")
print(pole)
print("licząc ze wzoru: ")
print(math.pi*0.5*0.5)

inside=monteCarlo(number,isSin)
pole = (inside / number)*2

print("sinusoida:")
print(pole)

