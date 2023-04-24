import os
from math import gcd, sqrt
from random import random, randint

import colorama
import numpy


# function generate two random numbers and check if they are coprime with each other
def randomNumbers1():
    abba = int(random() * 1000000000000)
    baab = int(random() * 1000000000000)
    return abba, baab


def randomNumbers2():
    abba = int(randint(0, 100000000000000000))
    baab = int(randint(0, 100000000000000000))
    return abba, baab


def coprime(a, b):
    return gcd(a, b) == 1


if __name__ == '__main__':
    wzglednie = 0
    colorama.init()
    n = 1000000
    for i in range(n):
        a, b=randomNumbers1()
        if coprime(a,b):
            wzglednie += 1
            # clean comment line
    print("1.: ", end='')
    print(wzglednie / n)
    p = sqrt(6 / (wzglednie / n))
    print(p)
    wzglednie = 0
    for i in range(n):
        a, b=randomNumbers2()
        if coprime(a,b):
            wzglednie += 1
            # clean comment line
    print("2.: ", end='')
    print(wzglednie / n)
    p = sqrt(6 / (wzglednie / n))
    print(p)
