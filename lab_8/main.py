# jarosław komsta
# 2022-05-24
from graphics import *





class map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.citys = []
        self.path=[]
        self.best_path=[]

    def _distanse(self,b, city):
        return ((b[0] - city[0]) ** 2 + (b[1] - city[1]) ** 2)** 0.5

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
        self.citys=sorted(self.citys, key=lambda x: x[0] + x[1])
        for city in self.citys:
            print(city)

    def finde_hamilton_path(self):
        #self.citys=sorted(self.citys, key=lambda x: x[0] + x[1])
        #print(self.citys)
        path = [self.citys[-1]]
        distance = 0
        for city in self.citys:
            path.append(city)
            distance+=self._distanse(path[-2], path[-1])
        distance+=self._distanse(path[0], path[-1])
        print(f"Distance: {distance}")
        self.path=path

    def finde_path(self):
        citys = {}
        distance = 0
        for city in self.citys:
            citys[city[2]] = city
        b=citys.pop(1)
        self.best_path.append(b)
        while len(citys)>1:
            min=[99999999,-1]
            for city in citys:
                if self._distanse(b,citys[city])<min[0]:
                    min=[self._distanse(b,citys[city]),city]
            self.best_path.append(citys[min[1]])
            try:
                b=citys.pop(min[1])
            except:
                print("No such city",min[1])
                print(citys)
                exit()
        for i in range(len(self.best_path)):
            distance+=self._distanse(self.best_path[i],self.best_path[i-1])
        print(f"Distance: {distance}")
        self.best_path.append(self.best_path[0])
        #print(self.best_path)


    def read_cities_from_file(self, filename):
        try:
            file = open(filename, "r")
            for line in file:
                buf = line.split()
                self.add_city([float(buf[1]),float( buf[2]), int(buf[0])])
            file.close()
        except:
            print("No such file")

    def print_map(self):
        scale_x = 12
        scale_y = 8
        workarea = GraphWin("Map", self.width*scale_x, self.height*scale_y)
        for city in self.citys:
            cir = Circle(Point(float(city[0])*scale_x,float(city[1])*scale_y ), 5)  # draw circle with center at middle of drawing area
            cir.setOutline("black")  # get a next outline color from color array
            cir.setWidth(2)  # set outline width
            cir.draw(workarea)  # draw the current circle
        for i in range(len(self.path) - 1):
            try:
                line = Line(Point(int(float(self.path[i][0]) * scale_x),
                                  int(float(self.path[i][1]) * scale_y)),
                            Point(int(float(self.path[i + 1][0]) * scale_x),
                                  int(float(self.path[i + 1][1]) * scale_y)))
                line.setOutline("red")
                line.setWidth(1)
                line.draw(workarea)
            except Exception as e:
                print(e)
                # print(self.citys[self.path[i]][0],end=" ")
                # print(self.citys[self.path[i]][1],end=" ")
                print(i, len(self.citys), self.path[i], self.path[i + 1])
        for i in range(len(self.best_path)-1):
            try:
                line = Line(Point(int(float(self.best_path[i][0])*scale_x),
                                  int(float(self.best_path[i][1])*scale_y)),
                            Point(int(float(self.best_path[i+1][0])*scale_x),
                                  int(float(self.best_path[i+1][1])*scale_y)))
                line.setOutline("blue")
                line.setWidth(1)
                line.draw(workarea)
            except Exception as e:
                print(e)
                # print(self.citys[self.path[i]][0],end=" ")
                # print(self.citys[self.path[i]][1],end=" ")
               # print(i,len(self.citys),self.best_path[i],self.best_path[i+1])


        try:
            workarea.getMouse()# get mouse to click on screen to exit
        except:
            pass
        workarea.close() # close the drawing window


if __name__ == "__main__":
    m = map(100, 100)
    m.read_cities_from_file("TSP.txt")
    m.finde_hamilton_path()
    m.finde_path()
    m.print_map()