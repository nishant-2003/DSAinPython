from binarySearchTree import print_BSTNode

class BSTNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        self.root= self.insert_helper(data , self.root)
    def insert_helper(self,data,node):
        if node is None:
            newNode= BSTNode(data)
            return newNode
        if data < node.data:
            node.left=self.insert_helper(data,node.left)
        else:
            node.right=self.insert_helper(data,node.right)
        return node


    def search(self,data):
        return self.searchHelper(data,self.root)

    def searchHelper(self,data,root):
        if root is None:
            return False
        if root.data == data:
            return True
        if data < root.data:
            return self.searchHelper(data,root.left)
        else:
            return self.searchHelper(data,root.right)
    def get_min_node(self,node):
        current=node
        while (current.left is not None):
            current=current.left
        return current
    def delete_helper(self,data,root):
        if root is None:
            return None
        if (data<root.data):
            root.left=self.delete_helper(data,root.left)
        elif(data>root.data):
            root.data=self.delete_helper(data,root.right)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            min_largest_node=self.get_min_node(root.right)
            root.data=min_largest_node.data
            root.right=self.delete(min_largest_node.data,root.right)

    def delete(self,data):
        return self.searchHelper(data,self.root)

bstObject= BST()
bstObject.insert(10)
bstObject.insert(20)
bstObject.insert(30)
bstObject.insert(40)
print_BSTNode(bstObject.root)