file = open("zadanie2.csv" ,"r")
data=[[]]
file.readline()
for line in file:
    data.append([int(line[0:line.find(",")]),line[line.find(",")+1::]])
    if(data[-1][1]=="\n"):
        data.remove(data[-1])
id=1
for d in data:
    d[0]=id
    id+=1
for d in data:
    d[1]=d[1].lower()
