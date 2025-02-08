import threading
import websockets
from enum import Enum
class Const(Enum):
    x = 1
    y = 2



class Data:
    __list = []

    def __init__(self, x, y, Const):
        self.x = x
        self.y = y
        self.Const = Const
        self.make()

    def make(self):
        for _ in range(0, 300):
            if self.Const == Const.x:
                self.y += 1
            else:
                self.x += 1
            self.__list.append(str(self.x) + " " + str(self.y))

    def getList(self):
        return self.__list



person1 = Data(3020561, 7621288, Const.x)

person2 = Data(3021221, 7621288, Const.x)

person4 = Data(3021227, 7621288, Const.x)

person3 = Data(3020565, 7621288, Const.x)

class Send:
    def __init__(self, list):
        self.list:list = list
        self.web = websockets.connect("ws://localhost:8765")

    def send(self):
        with websockets.connect("ws://localhost:8765") as t:
            t.send(self.list.pop())

    def read(self):
        self.web.recv()

    def start(self):
        threading.Thread(target=self.send).start()
        threading.Thread(target=self.send).start()

Send(person1.getList()).start()