import time
import random

from lab_6.TabTree import TabTree

if __name__ == '__main__':
    n = 500000
    print(n, end='\t')
    A = TabTree()
    start = time.time_ns()
    for i in range(n):
        A.INSERT(random.randint(0,int(n/4)) / 100.0)
    end = time.time_ns()
    print( end - start,end='\t')
    start = time.time_ns()
    for i in range(n):
        A.SEARCH(random.randint(0, int(n/4)) / 100.0)
    end = time.time_ns()
    print(end - start,end='\t')
    start = time.time_ns()
    for i in range(n):
        A.MIN(random.randint(0, int(n/4)) / 100.0)
    end = time.time_ns()
    print(end - start,end='\t')
    start = time.time_ns()
    for i in range(n):
        A.MAX(random.randint(0, int(n/4)) / 100.0)
    end = time.time_ns()
    print(end - start)
    A.read()
