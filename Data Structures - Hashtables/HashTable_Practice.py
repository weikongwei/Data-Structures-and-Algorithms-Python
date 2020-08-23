# NOT COMPLETED

from random import randint

class HashTable():

    def __init__(self, size=50):
        self.data = [""] * size
        self.addr_list = []

    def hash(self):
        while True:
            x = randint(0, len(self.data)-1)
            if x not in self.addr_list:
                return x

    def set(self, key, value):
        index = self.hash()
        self.data[index] = [key, value]
        self.addr_list.append(index)

    def get(self, key):
        for i in self.addr_list:
            if self.data[i][0] == key:
                return self.data[i][1]

    # def keys(self):
    #     keys = []
    #     for




if __name__ == "__main__":
    h = HashTable(50)
    h.set('grapes', 1000)
    h.set('apples', 10)
    h.set('oranges', 300)
    h.set('bananas', 200)
    x = h.get('grapes')
    # # key_arr = h.keys()
    print(h)
    print(x)
    # # print(key_arr)