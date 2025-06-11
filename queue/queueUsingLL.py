class node:
    def __init__(self,value):
        self.value=value
        self.next=None

class queueUsingLL:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def isEmpty(self):
        return self.size==0
    def size(self):
        return self.length

    def enqueue(self,data):
        new_node=node(data)
        self.length+=1

        if self.head is None:#as of now queue is empty
            self.head=new_node
            self.tail=new_node

        else:
            self.tail.next=new_node
            self.tail=new_node

        return f"added {data} to the queue"
    def front(self):
        if self.isEmpty():
            print("empty queue")
        return self.head.value

    def dequeue(self):
        if self.isEmpty():
            print("empty queue")
            return None
        self.length-=1
        data=self.head.value
        self.head=self.head.next
        if self.head is None:
            self.tail=None
        return data

queue = queueUsingLL()
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)
queue.enqueue(70)
print(queue.size())
queue.dequeue()
queue.dequeue()
print(queue.size())
print(queue.front())





