# jarosław komsta
# 2022-05-24
from graphics import *


class map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.citys = []
        self.path = []
        self.best_path = []

    def _distanse(self, b, city):
        return ((b[0] - city[0]) ** 2 + (b[1] - city[1]) ** 2) ** 0.5

    # citi is a list with stucture [x,y,name]
    def add_city(self, city):
        try:
            float(city[0])
            float(city[1])
            int(city[2])
            self.citys.append(city)
        except:
            try:
                print("Wrong city format for citi", city[2])
            except:
                print("Wrong city format")

    def print_cities(self):
        self.citys = sorted(self.citys, key=lambda x: x[0] + x[1])
        for city in self.citys:
            print(city)

    def finde_hamilton_path(self):
        # self.citys=sorted(self.citys, key=lambda x: x[0] + x[1])
        # print(self.citys)
        path = [self.citys[-1]]
        distance = 0
        for city in self.citys:
            path.append(city)
            distance += self._distanse(path[-2], path[-1])
        distance += self._distanse(path[0], path[-1])
        print(f"Distance: {distance}")
        self.path = path

    def finde_path(self, n):
        citys = {}
        distance = 0
        for city in self.citys:
            citys[city[2]] = city
        b = citys.pop(n)
        self.best_path.append(b)
        while len(citys) > 1:
            min = [99999999, -1]
            for city in citys:
                if self._distanse(b, citys[city]) < min[0]:
                    min = [self._distanse(b, citys[city]), city]
            self.best_path.append(citys[min[1]])
            try:
                b = citys.pop(min[1])
            except:
                print("No such city", min[1])
                print(citys)
                exit()
        for i in range(len(self.best_path)):
            distance += self._distanse(self.best_path[i], self.best_path[i - 1])
        # print(f"Distance: {distance}")
        return distance
        self.best_path.append(self.best_path[0])
        # print(self.best_path)

    def finde_path2(self):
        citys = {}
        distance = 0
        for city in self.citys:
            citys[city[2]] = city
        b = citys.pop(1)
        self.best_path.append(b)
        while len(citys) > 1:
            max = [0, -1]
            for city in citys:
                if self._distanse(b, citys[city]) > max[0]:
                    max = [self._distanse(b, citys[city]), city]
            self.best_path.append(citys[max[1]])
            try:
                b = citys.pop(max[1])
            except:
                print("No such city", max[1])
                print(citys)
                exit()
        for i in range(len(self.best_path)):
            distance += self._distanse(self.best_path[i], self.best_path[i - 1])
        print(f"Distance: {distance}")
        self.best_path.append(self.best_path[0])
        # print(self.best_path)

    def finde_path3(self):
        citys = {}
        distance = {}
        for city in self.citys:
            distance[city[2]] = (99999999, -1)
            citys[city[2]] = city
        # prim
        distance[1] = [0, 0]
        while len(citys) > 0:
            T = [99999999, 0]
            for city in distance:
                if distance[city][0] < T[0] and city in citys:
                    T = [distance[city][0], city]
            citys.pop(T[1])
            dis =999999999
            for city in citys:
                dis = self._distanse(citys[city], self.citys[T[1]-1])

                print (dis, citys[city],self.citys[T[1]-1])
                if dis ==0:
                    dis=999999
                if dis < distance[city][0]:
                    distance[city] = [dis, T[1]]
        print(distance)
        self.spanning_tree = distance


    def read_cities_from_file(self, filename):
        try:
            file = open(filename, "r")
            for line in file:
                buf = line.split()
                self.add_city([float(buf[1]), float(buf[2]), int(buf[0])])
            file.close()
        except:
            print("No such file")

    def print_map(self):
        scale_x = 10
        scale_y = 6
        workarea = GraphWin("Map", self.width * scale_x, self.height * scale_y)
        for city in self.citys:
            cir = Circle(Point(float(city[0]) * scale_x, float(city[1]) * scale_y),
                         5)  # draw circle with center at middle of drawing area
            cir.setOutline("black")  # get a next outline color from color array
            cir.setWidth(2)  # set outline width
            cir.draw(workarea)  # draw the current circle
        for i in range(len(self.path) - 1):
            try:
                line = Line(Point(int(float(self.path[i][0]) * scale_x),
                                  int(float(self.path[i][1]) * scale_y)),
                            Point(int(float(self.path[i + 1][0]) * scale_x),
                                  int(float(self.path[i + 1][1]) * scale_y)))
                line.setOutline("white")
                line.setWidth(1)
                line.draw(workarea)
            except Exception as e:
                print(e)
                # print(self.citys[self.path[i]][0],end=" ")
                # print(self.citys[self.path[i]][1],end=" ")
                print(i, len(self.citys), self.path[i], self.path[i + 1])
        for i in range(len(self.best_path) - 1):
            try:
                line = Line(Point(int(float(self.best_path[i][0]) * scale_x),
                                  int(float(self.best_path[i][1]) * scale_y)),
                            Point(int(float(self.best_path[i + 1][0]) * scale_x),
                                  int(float(self.best_path[i + 1][1]) * scale_y)))
                line.setOutline("blue")
                line.setWidth(1)
                line.draw(workarea)
            except Exception as e:
                pass
                # print(self.citys[self.path[i]][0],end=" ")
                # print(self.citys[self.path[i]][1],end=" ")
            # print(i,len(self.citys),self.best_path[i],self.best_path[i+1])
        try:
            for city in self.spanning_tree:
                try:

                    line = Line(Point(int(float(self.citys[self.spanning_tree[city][1]][0]) * scale_x),
                                      int(float(self.citys[self.spanning_tree[city][1]][1]) * scale_y)),
                                Point(int(float(self.citys[city][0]) * scale_x),
                                      int(float(self.citys[city][1]) * scale_y)))
                    line.setOutline("green")
                    line.setWidth(1)
                    line.draw(workarea)
                except:
                    pass
        except: pass
        try:
            workarea.getMouse()  # get mouse to click on screen to exit
        except:
            pass
        workarea.close()  # close the drawing window


if __name__ == "__main__":
    m = map(100, 100)
    m.read_cities_from_file("TSP.txt")
    m.finde_hamilton_path()
    # m.finde_path3()
    dis=100000000
    n=0
    for i in range(1,99):
        d = m.finde_path(i)

        print(d)
        if d<dis:
            dis=d
            n=i
            p=m.best_path
        m.best_path=[]
    print(dis,n)
    m.best_path=p
    m.print_map()
