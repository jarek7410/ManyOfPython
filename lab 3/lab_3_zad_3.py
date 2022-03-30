import math
from math import sqrt
from random import random


def isCircle(x,y,r,tryX,tryY):

    return r >= sqrt(abs((tryX - x) * (tryX - x) + (tryY - y) * (tryY - y)))

inside=0
number=1000000
for i in range(number):
    if(isCircle(1,1,0.5,random(),random())):
        inside+=1
pole=(inside/number)/(0.25*0.25)
print(pole)
print(math.pi)
pole=abs(pole-math.pi)
print("delta: ",end="")
print(pole)