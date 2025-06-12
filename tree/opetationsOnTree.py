from collections import deque
from tree import *
# def takeInputRecursively():
#     data=int(input("Enter the data for the node:"))
#     node=tree_node(data)
#     num_children=int(input(f"Enter the number of children for {data}"))
#     for _ in range(num_children):
#         childs=takeInputRecursively()
#         node.child.append(childs)
#     return node
# root=takeInputRecursively()
# print_tree_detailed(root)

def take_input_levelwise():
    data=int (input ("Enter the root data: "))
    root= tree_node(data)
    queue=deque()
    queue.append(root)
    while queue:
        current_node=queue.popleft()
        num_children=int(input(f"Enter the number of children for {current_node}" ))
        for i in range(num_children):
            child_data=int(input(f"Enter the data of the {i+1} child of {current_node}: "))
            child_node=tree_node(child_data)
            current_node.child.append(child_node)
            queue.append(child_node)
    return root

def count_nodes(root ):
    if root is None:
        return 0
    numberNodes=1
    for eachChild in root.child:
        numberNodes =numberNodes+count_nodes(eachChild)
    return (numberNodes)

def height_of_tree(root):
    if root is None:
        return 0
    height=1
    max_height=0
    for Child in root.child:
        max_height=max(max_height,height_of_tree(Child))
        height=height+max_height
    return height




root = take_input_levelwise()
print_tree_detailed(root)
print(count_nodes(root))
print(height_of_tree(root))