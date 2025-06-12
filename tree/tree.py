class tree_node:
    def __init__(self,data):
        self.data=data
        self.child=[]
    def __repr__(self):
        return f"{self.data}"
    def __str__(self):
        return f"{self.data}"

def print_tree(root):
    print(root.data)
    for child in root.child:
        print_tree(child)

def print_tree_detailed(root):
    if root is None:
        return None
    print(f"{root.data}:",end="")
    for child in root.child:
        print(child.data,end=",")
    print()
    for child in root.child:
        print_tree_detailed(child)
    return root

# root=tree_node(1)
# child1=tree_node(2)
# child2=tree_node(3)
# child3=tree_node(4)
# root.child.append(child1)
# child1.child.append(child2)
# root.child.append(child3)
#
print_tree(root)
print()
print_tree_detailed(root)
