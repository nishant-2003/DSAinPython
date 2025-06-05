from python.linkedList.linked_list import *
def mid_using_twopointer(head):
    if head is None or head.next is None:
        return head
    slow=head
    fast=head
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
    return slow.data
list=create_using_list([23,53,63,26,65])
print(mid_using_twopointer(list))

