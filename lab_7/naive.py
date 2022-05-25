class naive:  # this class is serching for pattern in table
    def __init__(self, table, pattern=None):
        self.pattern_y = None
        self.pattern_x = None
        self.table = table
        self.pattern = pattern

    def set_pattern(self, pattern):  # patern is a 2d table
        self.pattern = pattern
        self.pattern_x = len(pattern)
        self.pattern_y = len(pattern[0])

    def search(self):
        results = []
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                if self.test_pattern(i, j):
                    results.append((i, j))
        self.results = results
        return results

    def test_pattern(self, x, y):
        try:
            i = self.table[x + self.pattern_x][y + self.pattern_y]
        except:
            return False

        for i in range(self.pattern_x):
            for j in range(self.pattern_y):
                if self.pattern[i][j] is None:
                    continue
                if self.pattern[i][j] != self.table[x + i][y + j]:
                    return False
        return True

    def print_result(self):
        print('Współzedne wystapień:')
        for i in self.results:
            print(i[0],end= ', ')
            print( i[1])
        print("liczba wystapień:")
        print(len(self.results))


def ToTable(buff):  # this function is converting string to 2d table
    table = [[]]
    j = 0
    for i in range(len(buff)):

        if buff[i] != '\n' and buff[i] != '\r'and buff[i] != '\t':
            try:
               table[j].append(buff[i])
            except:
                pass
        elif buff[i] == '\r':
            continue
        elif buff[i] == '\t':
            table[j].append(None)
        else:
            table.append([])
            j += 1
    table.pop()

    # print(table)
    return table


if __name__ == '__main__':
    f = open('patterns/1000_pattern.txt')
    text = ToTable(f.read())
    f.close()
    n = naive(text)
    # n.set_pattern([["A", 'B', 'C'], ['B', None, None], ['C', None, None]])
    n.set_pattern(ToTable("ABC\nB\t\t\nC\t\t\n"))
    n.search()
    n.print_result()
