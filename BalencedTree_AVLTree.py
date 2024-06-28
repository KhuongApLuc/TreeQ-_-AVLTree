import os
os.system('cls')

#cây nhị phân cân bằng : cây con bên trái và cây con bên phải của 1 nút bất kì có chiều cao khác nhau không quá 1

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1 

class Tree:
    def __init__(self):
        self.root = None

    def _getHeight(self,node):
        if not node:
            return 0
        else: 
            return node.height
    def getHeight(self):
        return self._getHeight(self.root)
        
    def get_balanced_factor(self,node):
        if not node:
            return 0
        else:
            balanced_factor = self._getHeight(node.left) - self._getHeight(node.right)
            return balanced_factor

    def insertNode(self,node,value):
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = self.insertNode(node.left, value)
        elif value > node.value :
            node.right = self.insertNode(node.right, value)
        node.height = 1 + max(self._getHeight(node.left), self._getHeight(node.right))
        balanced_factor = self.get_balanced_factor(node)
        if balanced_factor < -1 :
            if value > node.right.value:
                return self.leftRotate(node)
            else:
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node)
        elif balanced_factor > 1:
            if value < node.right.value:
                return self.rightRotate(node)
            else:
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)
        return node    
    def leftRotate(self,node):
        if node:
            root = node.right
            node.right = root.left
            root.left = node
            node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
            root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
            return root
        
    def rightRotate(self,node):
        if node:
            root = node.left
            node.left = root.right
            root.right = node
            node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
            root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
            return root

    def deleteNode(self,node, value):
        if not node:
            return node
        elif value < node.value:
            node.left = self.deleteNode(node.left, value)
        elif value > node.value:
            node.right = self.deleteNode(node.right, value) 
        else: 
            print('found')
            if node.left is None :
                t = node.right
                node = None
                return t
            if node.right is None:
                t = node.left
                node = None
                return t
            temp = self.getSuccessor(node.right)
            node.value = temp.value
            node.right = self.deleteNode(node.right, node.value)    
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        balanced_factor = self.get_balanced_factor(node)
        if balanced_factor < -1 :
            if self.get_balanced_factor(node.right) <= 0:
                return self.leftRotate(node)
            else:
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node)
        elif balanced_factor > 1:
            if self.get_balanced_factor(node.left) >= 0:
                return self.rightRotate(node)
            else:
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)
        return node    
    
    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def _getSuccessor(self,node):
        if node is None or node.left is None:
            return node.value
        else:
            return self._getSuccessor(node.left)  
    def getSuccessor(self):
        return self._getSuccessor(self.root)      



bst = Tree()    
bst.insert(8)
bst.insert(4)
bst.insert(12)
bst.insert(2)
bst.insert(1)
bst.insert(3)
bst.insert(6)
bst.insert(5)
bst.insert(7)
bst.insert(10)
bst.insert(9)
bst.insert(11)
bst.insert(14)
bst.insert(13)
bst.insert(15)
print(bst.get_balanced_factor())