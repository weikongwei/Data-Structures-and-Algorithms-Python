# 15 --> 6 --> 8

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        temp = Node(value)
        self.tail.next = temp
        self.tail = temp
        self.length += 1

    def prepend(self, value):
        tem = Node(value)
        tem.next = self.head
        self.head = tem
        self.length += 1

    def showlist(self):
        node = self.head
        result = []
        while node != None:
            result.append(node.value)
            node = node.next
        print(" ".join(map(str,result)))
        print("Length of the list: ", self.length)
        return result

    def insert(self,index,value):
        if index == 0 :
            self.prepend(value)
            return
        if index == self.length -1:
            self.append(value)
            return

        newNode = Node(value)
        node = self.head
        for i in range(index-1):
            node = node.next
        newNode.next = node.next
        node.next = newNode
        self.length += 1

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        node = self.head
        for i in range(index-1):
            node = node.next
        if index == self.length-1:
            node.next = None
            self.tail = node
            self.length -= 1
            return
        node.next = node.next.next
        self.length -= 1

    def reverse(self):

        ## Brute Method: reasign values
        # if self.length == 1:
        #     return
        #
        # values = self.showlist()
        # values.reverse()
        #
        # node = self.head
        # for i in range(self.length):
        #     node.value = values[i]
        #     node = node.next
        # self.showlist()

        ## Reverse Pointer Method
        self.tail = self.head
        current = self.head
        previous = None
        next = current.next

        while current is not None: # if current exist, set next to current.next, previous to current, current to next
            next = current.next
            current.next = previous
            previous = current
            current = next
            # if next is not None:
            #     next = next.next
        self.head = previous




if __name__ == "__main__":
    linkedList = LinkedList(10)
    linkedList.append(5)
    linkedList.append(16)
    linkedList.prepend(1)
    linkedList.insert(1,2)
    linkedList.insert(0,0)
    linkedList.insert(linkedList.length-1,1000)
    linkedList.remove(5)
    linkedList.remove(0)
    linkedList.remove(linkedList.length-1)
    linkedList.showlist()
    linkedList.reverse()
    linkedList.showlist()



































# 10->5->16

# class Node():
#
#   def __init__(self,data):
#     self.data = data
#     self.next = None
#
# class LinkedList():
#
#   def __init__(self):
#     self.head = None
#     self.tail = None
#
#   def append(self,data):
#     new_node = Node(data)
#     if self.head == None:
#       self.head = new_node
#       self.tail = self.head
#       self.length = 1
#     else:
#       self.tail.next = new_node
#       self.tail = new_node
#       self.length += 1
#
#   def prepend(self,data):
#     new_node = Node(data)
#     new_node.next = self.head
#     self.head = new_node
#
#
#     self.length += 1
#
#   def insert(self,index,data):
#     new_node = Node(data)
#     i = 0
#     temp = self.head
#     if index>=self.length:
#       self.append(data)
#       return
#     if index ==0:
#       self.prepend(data)
#       return
#     while i<self.length:
#       if i == index-1:
#         temp.next , new_node.next = new_node , temp.next
#         self.length+=1
#         break
#       temp = temp.next
#       i+=1
#
#
#   def remove(self,index):
#     temp = self.head
#     i=0
#     if index>self.length:
#       print("Entered wrong index")
#
#     while i<self.length:
#       if index == 0:
#         self.head = temp.next
#         self.length -= 1
#         break
#       if i == self.length-1:
#         temp.next = None
#         self.tail = temp
#         self.length -= 1
#         break
#       if i == index-1:
#         temp.next = temp.next.next
#         self.length-=1
#         break
#       i+=1
#       temp = temp.next
#
#   def printl(self):
#     temp = self.head
#     while temp != None:
#       print(temp.data , end = ' ')
#       temp = temp.next
#     print()
#     print('Length = '+str(self.length))
#
#   def reverse(self):
#     prev = None
#     self.tail = self.head
#     while self.head != None:
#       temp = self.head
#       self.head = self.head.next
#       temp.next = prev
#       prev = temp
#     self.head = temp
#
#
# l = LinkedList()
# l.append(10)
# l.append(5)
# l.append(6)
# l.prepend(1)
# l.insert(2,99)
# l.insert(34,23)
# #l.remove(4)
# l.reverse()
# l.printl()
