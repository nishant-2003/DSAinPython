class stackUsingList:
    def __init__(self):
        self.__stack=[] #very important to make it private so that functionality is right

    def push(self,data):
        self.__stack.append(data)
        print(f"pushed {data} into stack")

    def size(self):
        return len(self.__stack)

    def is_empty(self):
        return len(self.__stack)==0

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        #return self.stack[len(self.stack)-1]
        return self.__stack[-1]
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.__stack.pop()


myStack=stackUsingList()
myStack.push(10)
myStack.push(11)
myStack.push(12)
myStack.push(13)
myStack.push(14)
print(myStack.peek())
print(myStack.pop())
print(myStack.peek())
