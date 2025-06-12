from collections import deque
from tree import *
def takeInputRecursively():
    data=int(input("Enter the data for the node:"))
    node=tree_node(data)
    num_children=int(input(f"Enter the number of children for {data}"))
    for _ in range(num_children):
        childs=takeInputRecursively()
        node.child.append(childs)
    return node
root=takeInputRecursively()
print_tree_detailed(root)

def take_input_levelwise():
    data=int (input ("Enter the root data: "))
    root= tree_node(data)
    queue=deque([root])
    while queue is not None:
        current_node=queue.popleft()
        num_children=int(input(f"Enter the number of children for {current_node}" ))
        for i in range(num_children):
            child_data=int(input(f"Enter the data of the {i+1} child of {current_node}: "))
            child_node=tree_node(child_data)
            current_node.child.append(child_node)
        queue.append(child_node)
    return root
queue=deque()

