class NodeQ:
    def __init__(a,data):
        a.data = data
        a.next = None

class MyQueue:
    def __init__(a):
        a.head = None
        a.tail = None
    
    def isEmpty(a):
        return a.head == None
    
    def EnQueue(a,data):
        node = NodeQ(data)
        if a.isEmpty():
            a.head = node
            a.tail = node
        else:
            a.tail.next = node
            a.tail = node
    
    def DeQueue(a):
        if a.isEmpty():
            return None
        data = a.head.data
        a.head = a.head.next
        return data

class Node:
    def __init__(a,data):
        a.data = data
        a.left = None
        a.right = None

class BSTree:
    def __init__(a):
        a.root = None
    def isEmpty(a):
        return a.root == None
    def insert(a,data):
        node = Node(data)
        if a.isEmpty():
            a.root = node
            return
        father = None
        cur = a.root
        while cur != None:
            if cur.data == data:
                print(f'key {data} da ton tai')
                return
            father = cur
            if cur.data < data:
                cur = cur.right
            else:
                cur = cur.left
        if father.data < data:
            father.right = node
        else:
            father.left = node
    def visit(a,p):
        if p == None:
            return
        print(f'{p.data} ',end = ' ')
    def preOrder(a,p):
        if p == None:
            return
        a.visit(p)
        a.preOrder(p.left)
        a.preOrder(p.right)
    def preVisit(a):
        a.preOrder(a.root)
    def postOrder(a,p):
        if p == None:
            return
        a.postOrder(p.left)
        a.postOrder(p.right)
        a.visit(p)
    def postVisit(a):
        a.postOrder(a.root)
    def inOrder(a,p):
        if p == None:
            return
        a.inOrder(p.left)
        a.visit(p)
        a.inOrder(p.right)
    def inVisit(a):
        a.inOrder(a.root)
    def breadth_first(a):
        if a.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(a.root)
        while not my.isEmpty():
            p = my.DeQueue()
            a.visit(p)
            if p.left != None:
                my.EnQueue(p.left)
            if p.right != None:
                my.EnQueue(p.right)

    
    def findFather(a,p):
        if not a.root or p == a.root.data: return
        cur = a.root
        father = None
        while cur:
            if p == cur.data: return father
            elif p > cur.data:
                father = cur
                cur = cur.right
            else:
                father = cur
                cur = cur.left
        return
    
    def deleteByMergingLeft(a,key):
        p = a.findNode(key)
        if p == None or p.left == None: return
        father = a.findFather(key)
        cur = p.left
        while cur.right != None:
            cur = cur.right #cur la gia trij ngoai cung ben phai cua con trai
        cur.right = p.right 
        if father == None:
            a.root = a.root.left
        else:
            if father.data < key :
                father.right = p.left
            else:
                father.left = p.left
##ver1
    def delCopy(a,data):
        grandfather = a.findFather(data)
        pos = a.findNode(data)
        cur = pos.left
        while cur:
            cur = cur.left
            pos = pos.left
        father = a.findFather(pos.data)
        father.right.left = grandfather.left.left
        father.right.right = grandfather.left.right
        grandfather.left = father.right
        father.right = None

###ver2
    def deletebycopyleft(a,p):
        q=a.findNode(p)
        if q==None or q.left==None:
            return
        cur=q.left
        father=q
        while cur.right!=None:
            father=cur
            cur=cur.right
        q.data=cur.data
        if q.left.right==None:
            q.left=q.left.left
        else:
            father.right=cur.left    
            
    def rightRotation(a,key):
        node = a.findNode(key)
        if node == None or node.left == None: return
        child = node.left
        temp = child.right
        child.right = node
        node.left = temp
        return child
    
    def rightRotate(a,key):
        father = a.findFather(key)
        if father == None:
            if a.root.data == key:
                a.root = a.rightRotation(key)
        else:
            if father.data < key:
                father.right = a.rightRotation(key)
            else:
                father.left = a.rightRotation(key)
        
    def leftRotation(a,key):
        node = a.findNode(key)
        if node == None or node.right == None: return
        child = node.right
        temp = child.left
        child.left = node
        node.right = temp
        return child
    
    def leftRotate(a,key):
        father = a.findFather(key)
        if father == None:
            if a.root.data == key:
                a.root = a.leftRotation(key)
        else:
            if father.data < key:
                father.left = a.leftRotation(key)
            else:
                father.right = a.leftRotation(key)
    
tree = BSTree()
tree.insert(8)
tree.insert(4)
# tree.insert(2)
tree.insert(12)
# tree.insert(3)
tree.insert(6)
tree.insert(10)
tree.insert(14)
# tree.insert(1)
tree.insert(13)
tree.insert(15)
tree.insert(5)
tree.insert(7)
tree.insert(9)
tree.insert(11)
# tree.preVisit()
# tree.rightRotate(4)
# print()
# tree.preVisit()
# tree.leftRotate(8)
# print()
# tree.preVisit()
tree.breadth_first()
print()
tree.deletebycopyleft(4)
tree.breadth_first()
