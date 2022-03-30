class TicTacToe:
    pola = [[0] * 3, [0] * 3, [0] * 3]
    """1 or -1"""
    whosemove = 1

    def decodePlayer(self, j):
        if (j == 0):
            return " "
        elif (j > 0):
            return "O"
        elif (j < 0):
            return "X"

    def show(self):
        for i in self.pola:
            print("--------------------------")
            for j in i:
                print("|", end="")
                print("  ", end=" ")
                print(self.decodePlayer(j), end="")
                print("  ", end=" ")
            print("|")
        print("--------------------------")

    def change(self, x, y):
        if (self.pola[x][y] == 0):
            self.pola[x][y] = self.whosemove
            self.whosemove = -1 * self.whosemove
            return 0
        else:
            return 1

    def winCheck(self):
        for i in range(3):
            suma1 = 0
            suma2 = 0
            for j in range(3):
                suma1 += self.pola[i][j]
                suma2 += self.pola[j][i]
            if (abs(suma1) == 3):
                print("wygrał: " + self.decodePlayer(suma1))
                return 0
            if (abs(suma2) == 3):
                print("wygrał: " + self.decodePlayer(suma2))
                return 0
        suma = self.pola[0][0] + self.pola[1][1] + self.pola[2][2]
        if (abs(suma) == 3):
            print("wygrał: " + self.decodePlayer(suma))
            return 0
        suma = self.pola[0][2] + self.pola[1][1] + self.pola[2][0]
        if (abs(suma) == 3):
            print("wygrał: " + self.decodePlayer(suma))
            return 0
        return 1

    def pcmove(self):
        exit =0
        for i in range(3):
            for j in range(3):
                if (self.change(i, j) == 0):
                    exit =1
                if(exit==1):
                    break
            if(exit==1):
                break
        return 0;

    def move(self, x, y, pc):
        if (self.change(x - 1, y - 1) == 1):
            print("wrong move")
        if (self.winCheck() == 1):
            if (pc):
                self.pcmove()
        self.show()
        return self.winCheck()


a = TicTacToe()
a.show()
while (True):
    i = input("chose move(two numbers between 1 and 3)[nr<space>nr]:\n")
    x = int(i[0])
    y = int(i[-1])
    if (a.move(x, y, True) == 0):
        break
