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

def insert_at_end_recursion(head,data):
    if head is None:
        newNode=node(data)
        return newNode
    # if head.next is None:
    #     newNode= node(data)
    #     head.next=newNode
    #     return head

    head.next=insert_at_end_recursion(head.next,data)
    return head

def insert_at_middle(head,data,index):
    if index == 0:
        return insert_at_begin(head,data)

    newNode = node(data)
    temp=head
    count=0
    while count is not None and count< index-1:
        temp=temp.next
        count+=1
    newNode.next=temp.next
    temp.next=newNode
    return head

def delete_from_end(head):
    if head is None:
        return None
    temp=head
    while temp.next.next is not None:
        temp=temp.next
    temp.next= None
    return head


def delete_form_middle(head,index):
    if head is None:
        return None
    if index==0:
        return head.next

    temp=head
    count=0
    while (temp is not None and count<index-1):
        temp=temp.next
        count+=1
    if (temp is None):
        print("out of bound")
        return head
    nodeTobeDeleted=temp.next
    nodeAfterDeletedNode=nodeTobeDeleted.next
    temp.next=nodeAfterDeletedNode
    return head



head=insert_at_begin(head,1)
print("\n")
display_ll(head)
tail=insert_at_end(head,6)
print("\n")
display_ll(head)
print()
tail_recurr=insert_at_end_recursion(head,5)
display_ll(head)
print()
middle=insert_at_middle(head,5,3)
display_ll(head)
delete_from_end(head)
print()
display_ll(head)
print()
delete_form_middle(head,3)
display_ll(head)