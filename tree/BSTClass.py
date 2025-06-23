class BSTNode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def add_child(self,data):
        if data ==self.data:
            return
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BSTNode(data)

        if  data>self.data:
            if data==self.data:
                return
            if data>self.data:
                if self.right:
                    self.right.add_child(data)
                else:
                    self.right=BSTNode(data)

    def in_order_traversal(self):
        element=[]
        if self.left:
            element+=self.left.in_order_traversal()
        element.append(self.data)
        if self.right:
            element+=self.right.in_order_traversal()
        return element


    def search(self,data):
        if data==self.data:
            return True
        if data<self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        else:
            if self.right:
                return self.right.search(data)
            else:
                return False
    def find_max(self):
        if self.right is None:
            return self.data
        ans= self.right.find_max()
        return ans
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


    def delete_node(self,data):
        if data<self.data:
            if self.left:
                self.left.delete_node(data)
        elif data > self.data:
            if self.right:
                self.right.delete_node(data)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_val= self.right.find_min()
            self.data=min_val
            self.right=self.right.delete_node(data)
        return self



def build_tree(element):
        root=BSTNode(element[0])
        for i in range(1,len(element)):
            root.add_child(element[i])
        return root
if __name__ == '__main__':
    numbers=[11,12,23,8,45,66,34,21]
    number_tree= build_tree(numbers)
    print(number_tree.in_order_traversal())
    print(number_tree.search(200))
    number_tree.delete_node(23)
    print(number_tree.in_order_traversal())
