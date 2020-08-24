class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left == None:
                    current.left = newNode
                    return
                current = current.left
            elif value > current.value:
                if current.right == None:
                    current.right = newNode
                    return
                current = current.right
            elif value == current.value:
                print("Duplicated value.")
                return


    def lookup(self,value): # to see if a value exists in a tree
        if self.root == None:
            print("Value doesn't exist")
            return False

        current = self.root
        while True:
            if value < current.value:
                if current.left == None:
                    print("Value doesn't exist")
                    return False
                current = current.left
            elif value > current.value:
                if current.right == None:
                    print("Value doesn't exist")
                    return False
                current = current.right
            elif value == current.value:
                print("Value found")
                return True

    def printTree(self):
        if self.root is not None:
          self.printTreeAuxillary(self.root)
        else:
          print("Tree is empty")
          return None

    # when trieversing a tree, always remenber left,value,right pattern
    def printTreeAuxillary(self,node):
        if node.left is not None:
            self.printTreeAuxillary(node.left)
        print(node.value)
        if node.right is not None:
            self.printTreeAuxillary(node.right)



if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(6)
    bst.insert(12)
    bst.insert(8)
    x = bst.lookup(6)
    print(x)
    y = bst.lookup(99)
    print(y)
    bst.printTree()




























# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# class BinarySearchTree:
#
#   def __init__(self):
#     self.root = None
#
#   def insert(self,data):
#     new_node = Node(data)
#     if self.root == None:
#       self.root = new_node
#       return
#     else:
#       curr_node = self.root
#       while True:
#         if data < curr_node.data:
#           #Left
#           if curr_node.left == None:
#             curr_node.left = new_node
#             return
#           else:
#             curr_node = curr_node.left
#         elif data > curr_node.data:
#             #Right
#             if curr_node.right == None:
#               curr_node.right = new_node
#               return
#             else:
#               curr_node = curr_node.right
#
#   def lookup(self,data):
#     curr_node = self.root
#     while True:
#       if curr_node == None:
#         return False
#       if curr_node.data == data:
#         return True
#       elif data < curr_node.data:
#         curr_node = curr_node.left
#       else:
#         curr_node = curr_node.right
#
#   def print_tree(self):
#     if self.root != None:
#       self.printt(self.root)
# #Inorder Traversal (We get sorted order of elements in tree)
#
#   def printt(self,curr_node):
#     if curr_node != None:
#       self.printt(curr_node.left)
#       print(str(curr_node.data))
#       self.printt(curr_node.right)
#
#
# bst = BinarySearchTree()
# bst.insert(10)
# bst.insert(5)
# bst.insert(6)
# bst.insert(12)
# bst.insert(8)
# x = bst.lookup(6)
# print(x)
# y = bst.lookup(99)
# print(y)
# bst.print_tree()
