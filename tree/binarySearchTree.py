class BSTNode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None


def take_input():
    data = int(input("Enter the data of the Node:\t"))
    if data == -1:
        return
    root = BSTNode(data)
    print(f"Enter the left child of {root.data}:\t")
    root.left=take_input()
    print(f"Enter the right child of {root.data}:\t")
    root.right=take_input()
    return root

def search(root,value):
    if root.data==value:
        print("Element Found")
    if root.data>value:
        search(root.left,value)
    else:
        search (root.right,value)


def isBST(root):
    pass


def print_BSTNode(root):
    if root is None:
        return
    print_BSTNode(root.left)
    print(root.data,end=", ")
    print_BSTNode(root.right)


def print_bst_in_range(root,low,high):
    if root is None:
        return
    if (low<root.data):
        print_bst_in_range(root.left,low,high)
    if (low<=root.data<=high):
        print(root.data, end=" ")
    if (high > root.data):
        print_bst_in_range(root.right,low,high)





root=take_input()
print_BSTNode(root)
print(search(root,20))
print(print_bst_in_range(root,20,40))
