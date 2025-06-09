class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stackUsingLL:
    def __init__(self):
        self.head=None
        self.length=0 #shows the total number of elements in the stack

    def push(self,data):
        new_node=Node(data)
        self.length+=1
        if self.head == None:
            self.head=new_node
            return f"Added {data}"

        new_node.next=self.head
        self.head=new_node
        return f"Added {data}"

    def peek(self):
        if self.head is None or self.length==0:
            return "Stack is empty"
        return self.head.data

    def pop(self):
        if self.head is None or self.length==0:
            return "Stack is empty"
        data_at_top=self.head.data
        self.head=self.head.next
        self.length-=1
        return data_at_top

    def size(self):
        return self.length

    def is_empty(self):
        return self.length==0

myStack=stackUsingLL()
print(myStack.push(10))
print(myStack.push(11))
print(myStack.push(12))
print(myStack.push(13))
print(myStack.push(14))
print(myStack.peek())
print(myStack.pop())
print(myStack.peek())
print(myStack.size())
print(myStack.pop())
