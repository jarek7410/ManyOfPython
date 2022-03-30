from array import *
import null as null

L = array('f', [1, 2])
for x in range(46):
    L.append(round(((L[-1] + L[-2]) / (L[-2] - L[-1])), 2))

suma = 0
sequence = 1
befor = null
table = {}

for i in L:
    try:
        table[i] = table[i] + 1
    except:
        table[i] = 1

suma = 0
moda = [0, []]
for i in table:
    suma += table[i] * i
    if (moda[0] <= table[i]):
        if (moda[0] < table[i]):
            moda = [table[i], [i]]
        else:
            moda[1].append(i)
print('srednia:', end="")
print((suma / 48.0))
if (moda[0] <= 1):
    print('brak mody')
else:
    print('moda jest: ', end='')
    for i in moda[1]:
        print(i, end=", ")
    print('\npowtarza sie: ', end="")
    print(moda[0])
print('elementy powtarzajace sie wiecej niz raz to:')
for i in table:
    if(table[i]>=2):
        print(i,end=", ")
