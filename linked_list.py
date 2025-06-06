class node:
    __slots__='data','next'
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next


def create_ll():
    data=int(input("Enter the element of the link list:-"))
    head=None
    tail=None
    while data is not -1:
        new_node = node(data)
        if head is None:
            head=new_node
            tail=new_node
        else:
            tail.next=new_node
            tail=new_node
        data = int(input("Enter the element of the link list:-"))
    return head
def create_using_list(nums):
    if not nums:
        return None
    head=node(nums[0])
    temp=head
    for items in nums[1:]:
        temp.next=node(items)
        temp=temp.next
    return head
def display_ll(head):
    temp = head
    while temp is not None:
        print(temp.data, end="->")
        temp=temp.next
    return

def lenght(head):#using iretation
    lenght_List=0
    temp=head
    while temp is not None:
        lenght_List+=1
        temp=temp.next
    return lenght_List

def length_using_recursion(head):
    if head is None:
        return 0
    length= length_using_recursion(head.next)
    return 1+length

# list=create_ll()
# display_ll(list)
# print("\n")
#
# print(lenght(list))
#
# print(length_using_recursion(list))
#





#ALTERTNATIVE WAY
# class node:
#     __slots__='data','next'
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
#
# def print_ll(head):
#     temp=head
#     while temp is not None:
#         print(temp.data,end="->")
#         temp=temp.next
#     return
#
#
# def create_ll():
#     data=int(input("Enter the data of the node:-"))
#     head=None
#     while data!=-1:
#         new_node=node(data)
#         if head is None :
#             head=new_node
#         else:
#             temp=head
#             while temp.next is not None:
#                 temp=temp.next
#             temp.next=new_node
#         data=int(input("Enter the data of the node:"))
#     return head
# newHead=create_ll()
# print_ll(newHead)
