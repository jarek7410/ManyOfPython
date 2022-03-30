import null as null

L = [1, 2]
for x in range(46):
    L.append(round(((L[-1] + L[-2]) / (L[-2] - L[-1])),2))

suma = 0
sequence = 1
befor = null
moda = [0, [0.0]]
L.sort()
for i in range(0, 48):
    suma += L[i]
    if (befor == null):
        befor = L[i]
    else:
        if (befor != L[i]):
            befor = L[i]
            sequence = 1
        else:
            sequence += 1
    if (sequence >= moda[0]):
        if (sequence == moda[0]):
            moda[1].append(L[i])
        else:
            moda[0] = sequence
            moda[1] = [L[i]]

print('srednia:',end="")
print((suma / 48.0))
if (moda[0] <= 1):
    print('brak mody')
else:
    print('moda jest: ', end='')
    for i in moda[1]:
        print(i, end=", ")
    print('\npowtarza sie: ',end="")
    print (moda[0])

print('elementy powtarzajace sie wiecej niz raz to:')

befor=null
for i in L:
    if(befor==null):
        befor = i
    else:
        if(befor==i):
            print(i,end=", ")
        else:
            befor=i
