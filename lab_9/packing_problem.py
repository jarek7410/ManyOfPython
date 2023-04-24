class backpack:
    def __init__(self, size_x, size_y, items):
        self.size_x = size_x
        self.size_y = size_y
        self.inside = []
        self.items = items  # list of items
        self.items_backuup = self.items.copy()
        for i in range(size_x):
            self.inside.append([])
            for j in range(size_y):
                self.inside[i].append(0)

    def print_inside(self):
        for i in self.inside:
            for j in i:
                print(j, end="\t")
            print()

    def packing_problem(self):
        for item in self.items:
            if self.items[item][1] <= self.size_x and self.items[item][2] <= self.size_y:
                for i in range(self.items[item][1]):
                    for j in range(self.items[item][2]):
                        self.inside[i][j] = self.items[item][0]
    def plecak(self):
        for notforuse in self.items:
            m=max(self.items, key=lambda x: self.items[x][3])


if (__name__ == "__main__"):
    #open file
    f = open("packages/packages20.txt", "r")
    #read file
    data={}
    f.readline()
    keywords = f.readline().split(",")
    for line in f:
        line = line[0:-1].split(",")
        data[line[0]] = [int(line[0]),int(line[1]), int(line[2]), int(line[3])]

    f.close()
    print(data)
    b = backpack(20, 20,data)
    b.packing_problem()
    b.print_inside()