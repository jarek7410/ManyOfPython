import time

a = 0
n=100000000
start = time.time()
tab = [2]*n
for i in tab:
    a+= i
end = time.time()
t1=end-start
start=time.time()
for i in range(n):
    a-=i
end = time.time()
t2 = end-start
print(" python for time: ",end="")
print(t1)
print("cpp for style time: ",end="")
print(t2)
print("doference: ",end="")
print(abs(t1-t2))
