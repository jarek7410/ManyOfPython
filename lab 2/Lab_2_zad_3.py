import time
from linecache import getline
from math import floor
from mmap import mmap

text=input()
fileName="SJP.txt"

if(text.strip().count(" ")>0):#zakładam że wyrazy podzielone sa tylko spacja
    print("nie jest to jeden wyraz")
else:
    text=text.lower()
    start = time.time()
    f=open(fileName,"r",encoding="utf-8")
    be=True
    print (text)
    for line in f:
        if(text in line):
            print("jest w spj")
            be=False
            break
    if(be):
        print("nie jest w sjp")
    stop = time.time()
    print("czas sprawdzania \"po kolei\" ", end="\t")
    print(stop - start)
    start=time.time()
    f=open(fileName,"r",encoding="cp1252",errors='ignore')
    lenOfF=2998088
    f.seek(0,0)

    def binserch(lenoff,f,w,p,q,iter):
        v=floor((p+q)/2)
        f.seek(v,0)
        t=str(f.readline())
        print(t,end=" ")
        if(p>=q):
            return False
        if(t==w):
            return True
        elif(t>w):
            return binserch(lenoff,f,w,p,v-1,iter+1)
        else:
            return binserch(lenoff,f,w,v+1,q,iter+1)
    if(binserch(lenOfF,f,text,0,lenOfF+1,1)):
        print("jest")
    else:
        print("nie ma")
    f.close()
    stop = time.time()
    print("czas sprawdzania \"test\" ", end="\t\t")
    print(stop - start)
    start = time.time()
    f = open(fileName, "r", encoding="utf-8", errors='ignore')

    p=0
    q=2998088 # magic number - last index of file
    while(p<q):
        v = floor((p + q) / 2)
        f.seek(v-2,0)

        t=f.readline()
        t=t.split("\n")
        #
        print(t)
        #t = t[1]
        if(t==text):
            print("jest")
            q=-3
            break
        elif(t>text):
            q=v-1
        else:
            p=v+1
    if(q!=-3):
        print("nie jest")

    f.close()
    stop = time.time()
    print("czas sprawdzania \"test2\" ", end="\t\t")
    print(stop - start)
