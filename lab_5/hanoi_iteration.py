def hanoi_iteration(param, tab):
    i = 0
    while 1 < len(tab) and len(tab[2]) < param and len(tab[1]) < param:
        i += 1
        tab[3]+=1
        if (i % 3 == 1):
            if (len(tab[0]) != 0 and (len(tab[2]) == 0 or tab[0][-1] < tab[2][-1])):
                #print('A -> C', end=f" {tab}\n")
                tab[2].append(tab[0].pop())
            else:
                #print("C -> A", end=f" {tab}\n")
                tab[0].append(tab[2].pop())
        elif (i % 3 == 2):
            if (len(tab[0]) != 0 and (len(tab[1]) == 0 or tab[0][-1] < tab[1][-1])):
                #print('A -> B', end=f" {tab}\n")
                tab[1].append(tab[0].pop())
            else:
                #print("B -> A", end=f" {tab}\n")
                tab[0].append(tab[1].pop())
        else:
            if (len(tab[2]) != 0 and (len(tab[1]) == 0 or tab[2][-1] < tab[1][-1])):
                #print('C -> B', end=f" {tab}\n")
                tab[1].append(tab[2].pop())
            else:
                #print("B -> C", end=f" {tab}\n")
                tab[2].append(tab[1].pop())


if (__name__ == "__main__"):
    stack = [[], [], [],0]
    n = 4
    for i in range(n):
        stack[0].append(n - i)
    print(stack)
    hanoi_iteration(n, stack)
    print(stack)
