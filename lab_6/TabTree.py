# tree on tab with numbers from .5 with step 1
class TabTree:
    class Tree:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

        def maxTree(self):
            if self.right is not None:
                return self.right.maxTree()
            else:
                return self.value

        def minTree(self):
            if self.left is not None:
                return self.left.minTree()
            else:
                return self.value

        def searchTree(self, y, root=True):
            if self.value == y:
                return True
            elif self.value > y:
                if self.left is not None:
                    return self.left.searchTree(y, False)
            else:
                if self.right is not None:
                    return self.right.searchTree(y, False)
            if root:
                return False

        def readTree(self, t="", lm=0):
            print((((len(t)) * lm) * " ") + f"{t}{self.value}", end="")
            if self.left is not None:
                self.left.readTree(t + "-", 0)

            if self.right is not None:
                if self.left is None:
                    self.right.readTree(t + "-", 0)
                else:
                    print(end="\n")
                    print(end=(len(t) * " "))
                    self.right.readTree(t + "-", len(f"{self.value}"))

        def writeToTree(self, value):
            if self.value == value:
                pass
            elif self.value < value:
                if self.right is None:
                    self.right = TabTree.Tree(value)
                else:
                    self.right.writeToTree(value)
            else:
                if self.left is None:
                    self.left = TabTree.Tree(value)
                else:
                    self.left.writeToTree(value)

    def __init__(self):
        self.tab = {}

    def write(self, value):
        i = int(value)
        if (i + .5) not in self.tab:
            self.tab[i + .5] = TabTree.Tree(i + .5)
        self.tab[i + .5].writeToTree(value)

    def read(self):
        for i in self.tab:
            self.tab[i].readTree()
            print()

    def INSERT(self, value):
        self.write(value)

    def SEARCH(self, value):
        i = int(value)
        if i + .5 in self.tab:
            return self.tab[i + .5].searchTree(value)
        else:
            return False

    def MIN(self, value):
        i = int(value)
        if i + .5 in self.tab:
            return self.tab[i + .5].minTree()
        else:
            Exception("Tree is empty")

    def MAX(self, value):
        i = int(value)
        if i + .5 in self.tab:
            return self.tab[i + .5].maxTree()
        else:
            Exception("Tree is empty")


if __name__ == "__main__":
    t = TabTree()
    t.write(1.3)
    t.write(1.6)
    t.write(3.7)
    t.write(4.0)
    t.write(4.99)
    t.write(7.3)
    t.write(7.8)
    t.write(7.7)
    t.write(7.6)
    t.write(7.9)
    t.write(9.3)
    t.read()
    if t.SEARCH(7.7):
        print("Found")
    else:
        print("Not found")
    print(t.MIN(7.7))
    print(t.MAX(7))
