class queue:
    def __init__(self):
        self.__queue=[]
    def size(self):
        return len(self.__queue)
    def is_empty(self):
        return self.size()==0
    def enqueue(self,data):
        return self.__queue.append(data)
    def dequeue(self):
        if self.size()== 0:
            return "no elements in queue"
        return self.__queue.pop(0)
    def peek(self):
        if self.size()== 0:
            return "no elements in queue"
        return self.__queue[0]


queue = queue()
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)
queue.enqueue(70)
print(queue.size())
queue.dequeue()
queue.dequeue()
print(queue.size())
print(queue.peek())