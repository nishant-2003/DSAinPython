from linked_list import *
def reverse_ll(head):
    if head is None or head.next is None:
        return head
    small_ans=reverse_ll(head.next)
    temp=small_ans
    while temp.next is not None:
        temp=temp.next
    temp.next=head
    head.next=None
    return small_ans


head1=create_using_list([3,4,6,8,1,5])
display_ll(reverse_ll(head1))
