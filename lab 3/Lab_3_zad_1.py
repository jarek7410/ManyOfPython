import glob
import os

src="zadanie1\\"
dst="zad1\\"
files =[]
for i in glob.glob(src+"*"):
    files.append(i.split("\\")[1])

try:
    os.mkdir(dst)
except:
    pass
for f in files:
    try:
        os.mkdir(dst+f[0])
    except:
        pass

        print("src: "+src+f+" dst: "+dst+f[0]+"\\"+f)
        os.rename(src+f,dst+f[0]+"\\"+f)

