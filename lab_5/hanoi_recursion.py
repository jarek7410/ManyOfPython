def hanoi_recursion(param, tab):
    towerNames = ["A", "B", "C"]
    stack = {towerNames[0]:tab[0],towerNames[1]:tab[1],towerNames[2]:tab[2],'n':tab[3]}
    hoirec(param, "A", "B", "C", stack)
def hoirec(param, a, b, c, t):
    if param == 1:
        t["n"] += 1
        t[c].append(t[a].pop())
        #print(f'{a} -> {c}',end=f' {t}\n')
    else:
        hoirec(param - 1, a, c, b, t)
        t["n"] += 1
        t[c].append(t[a].pop())
       # print(f'{a} -> {c}',end=f' {t}\n')
        hoirec(param - 1, b, a, c, t)


if(__name__ == "__main__"):
    towerNames = ["A", "B", "C"]
    n=4
    stack = {towerNames[0]:[],towerNames[1]:[],towerNames[2]:[],'n':0}
    for i in range(n):
        stack[towerNames[0]].append(n - i)
    print (stack)
    rec = {towerNames[0]:n,towerNames[1]:0,towerNames[2]:0,'n':0}
    hoirec(n, towerNames[0], towerNames[1], towerNames[2], stack)
    print(rec)

