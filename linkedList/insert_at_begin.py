from python.linkedList.linked_list import node,create_ll,display_ll
head=create_ll()
display_ll(head)
def insert_at_begin(head,data):
    newNode=node(data)
    newNode.next=head
    head=newNode
    return head


def insert_at_end(head,data):
    newNode=node(data)
    if head is None:
        return newNode
    temp=head
    while temp.next is not None:
        temp=temp.next
    temp.next=newNode
    tail=newNode
    return head


head=insert_at_begin(head,1)
print("\n")
display_ll(head)
tail=insert_at_end(head,6)
print("\n")
display_ll(head)

#OUTPUT
# Enter the element of the link list:-1
# Enter the element of the link list:-2
# Enter the element of the link list:-3
# Enter the element of the link list:--1
# 1->2->3->
#
# 1->1->2->3->
#
# 1->1->2->3->6->