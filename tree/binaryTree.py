from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def __repr__(self):
        return f"{self.data}"



def take_input():
    data=int(input("Enter the data for the node:"))
    if data == -1:
        return None
    root = Node(data)
    print(f"The left child of {data}")
    root.left=take_input()
    print(f"The right child of {data}")
    root.right=take_input()
    return root




def take_input_levelwise():
    data=int(input("Enter the data for the Node:\t"))
    if data ==-1:
        return None
    root=Node(data)
    queue=deque([root])
    while len(queue)!=0:
        current_child=queue.popleft()
        left_child=int(input ( f"Enter the left child of {current_child.data}"))
        if left_child != -1:
            left_node=Node(left_child)
            current_child.left=left_node
            queue.append(left_node)

        right_child=int(input(f"Enter the right child of {current_child.data}"))
        if right_child != -1:
            right_node=Node(right_child)
            current_child.right=right_node
            queue.append(right_node)
    return root



def height(root):
    if root is None:
        return 0
    left_height=height(root.left)

    right_height=height(root.right)
    heightOfTree=1+max(left_height,right_height)
    return heightOfTree




def diameter(root):
    if root is None:
        return 0
    leftHeight=height(root.left)
    rightHeight=height(root.right)
    left_diameter=diameter(root.left)
    right_diameter=diameter(root.right)
    ans=max(left_diameter,right_diameter,leftHeight+rightHeight)
    return ans


#SOLVE IT AGAIN
# def diameter_of_tree_optimized(root):
#     if root is None:
#         return 0
#     left_height,left_diameter=diameter_of_tree_optimized(root.left)
#     right_height,right_diameter=diameter_of_tree_optimized(root.right)
#     diameter_thorough_root=left_height+right_height
#     #left_diameter
#     #right_diameter
#     ans_diameter=max(diameter_thorough_root,left_diameter,right_diameter)
#     current_tree_height=1+max(left_height,right_height)
#     return current_tree_height,ans_diameter



def is_balanced_tree(root):
    pass





def print_data(root):
    if root is None:#Base Case
        return
    print(root.data,end="\t:\t")
    if root.left is not None:
        print(f"Left->{root.left.data}",end=",")
    else:
        print(f"Left->{None}",end=",")
    if root.right is not None:
        print(f"Right->{root.right.data}")
    else:
        print(f"Right->{None}")
    print_data(root.left)
    print_data(root.right)

def preorder_traversal(root):
    if root is None:
        return 0
    print(root.data, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)
    return None


def postorderTraversal(root):
    if root is None:
        return 0
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print(root.data, end=" ")
    return None

def InOrderTraversal(root):
    if root is None:
        return 0
    postorderTraversal(root.left)
    print(root.data, end=" ")
    postorderTraversal(root.right)

    return None




print("Enter the data for binary tree (-1 for no node)")
root=take_input_levelwise()
print_data(root)
print(preorder_traversal(root))
print(postorderTraversal(root))
print(InOrderTraversal(root))