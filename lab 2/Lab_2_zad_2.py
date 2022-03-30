file = open("zadanie2.csv", "r")
file.readline()  # pomijanie nagłówku
dict = {}
table = []
for line in file:
    v = line.find(",")
    text = line[v + 1::]
    if (text != "\n"):
        id = line[0:v]
        text = text.lower()
        table.append([int(id), text])
table.sort()

for i in table:
    while (i[0] in dict):
        i[0] += 1
    dict[i[0]] = i[1]

for i in dict:
    s = dict[i].split(" ")
    for word in s:
        try:#wyjątek wyskakuje kiedy sa wyrazy jednoznakowe
            if abs(ord(word[0]) - ord(word[1])) == 1:
                print(word, end=" id:")
                print(i,end=", ")
                word = ""
        except:
            print(end="")
    print()
file.close()
