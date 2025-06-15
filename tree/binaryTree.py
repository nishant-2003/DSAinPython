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

print("Enter the data for binary tree (-1 for no node)")
root=take_input_levelwise()
print_data(root)