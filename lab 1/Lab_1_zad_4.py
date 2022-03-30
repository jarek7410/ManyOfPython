tab = [1,2,3]
try:
    print(tab[3])
except:
    print("IndexError")
try:
    a = 100
    a = a / (a-a)
except:
    print("ZeroDivisionError")
try:
    print(bb)
except:
    print("NameError")