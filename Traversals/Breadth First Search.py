class Node():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        current_node = self.root
        if self.root == None:
            self.root = new_node
        else:
            while current_node.value != None:
                if val > current_node.value:
                    if current_node.right == None:
                        current_node.right = new_node
                        break
                    current_node = current_node.right
                    continue

                if val < current_node.value:
                    if current_node.left == None:
                        current_node.left = new_node
                        break
                    current_node = current_node.left
                    continue

                if val == current_node.value:
                    return print('Duplicated value')


    def lookup(self, val):
        if self.root == None:
          return print('Tree is empty')
        else:
            current_node = self.root

            while current_node.value != None:
                if val > current_node.value:
                    if current_node.right == None:
                        return print("Value not found")
                    current_node = current_node.right
                    continue

                if val < current_node.value:
                    if current_node.left == None:
                        return print("Value not found")
                    current_node = current_node.left
                    continue

                if val == current_node.value:
                    return print('Value found!!!')


    def breadthfirstsearch(self):
        lst = []
        queue = [self.root]

        while len(queue) != 0:
            current_node = queue[0]
            # print(current_node.value)
            lst.append(current_node.value)
            if current_node.left != None:
                queue.append(current_node.left)
            if current_node.right != None:
                queue.append(current_node.right)
            del queue[0]

        return lst

    def recursivebfs(self, queue, mylist):
        if len(queue) == 0:
          return mylist

        current_node = queue[0]
        mylist.append(current_node.value)
        if current_node.left != None:
          queue.append(current_node.left)
        if current_node.right != None:
          queue.append(current_node.right)
        del queue[0]

        return self.recursivebfs(queue,mylist)


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)


# tree.lookup(100)
print(tree.breadthfirstsearch())
print(tree.recursivebfs([tree.root], []))


# Solution:

# class Node:
#   def __init__(self,val):
#     self.val = val
#     self.left = None
#     self.right = None
#
# class BinarySearchTree:
#   def __init__(self):
#     self.root = None
#
#   def insert(self,val):
#     new_node = Node(val)
#     if self.root == None:
#       self.root = new_node
#       return
#     temp = self.root
#     while True:
#       if new_node.val < temp.val:
#         if temp.left == None:
#           temp.left = new_node
#           break
#         else:
#           temp = temp.left
#       elif new_node.val > temp.val:
#         if temp.right == None:
#           temp.right = new_node
#           break
#         else:
#           temp = temp.right
#
#   def lookup(self,val):
#     temp = self.root
#     while True:
#       if temp.val == val:
#         return True
#       elif temp == None:
#         return False
#       elif val < temp.val:
#         temp = temp.left
#       elif val > temp.val:
#         temp = temp.right
#
#   def breadthfirstsearch(self):
#     currnode = self.root
#     mylist = []
#     queue = []
#     queue.append(currnode)
#
#     while len(queue) > 0:
#       currnode = queue[0]
#       del queue[0]
#       mylist.append(currnode.val)
#       if currnode.left:
#         queue.append(currnode.left)
#       if currnode.right:
#         queue.append(currnode.right)
#
#     return mylist
#
#   def recursivebfs(self,queue,mylist):
#     if len(queue) == 0:
#       return mylist
#     currnode = queue[0]
#     del queue[0]
#     mylist.append(currnode.val)
#     if currnode.left:
#       queue.append(currnode.left)
#     if currnode.right:
#       queue.append(currnode.right)
#
#     return self.recursivebfs(queue,mylist)
#
#
#
# tree = BinarySearchTree()
# tree.insert(9)
# tree.insert(4)
# tree.insert(6)
# tree.insert(20)
# tree.insert(170)
# tree.insert(15)
# tree.insert(1)
#
# x = tree.lookup(170)
# print(x)
# print(tree.breadthfirstsearch())
# print(tree.recursivebfs([tree.root],[]))
