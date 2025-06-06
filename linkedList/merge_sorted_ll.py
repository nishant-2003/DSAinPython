from linked_list import *

def merge_sorted_ll(head1, head2):
    final_head = None
    final_tail = None

    if head1 is None:
        return head2
    if head2 is None:
        return head1

    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            node = head1
            head1 = head1.next
        else:
            node = head2
            head2 = head2.next

        if final_head is None:
            final_head = node
            final_tail = node
        else:
            final_tail.next = node
            final_tail = node

    # Attach remaining nodes
    if head1 is not None:
        final_tail.next = head1
    if head2 is not None:
        final_tail.next = head2

    return final_head

# Sample usage
head1 = create_using_list([2, 4, 5, 6, 7, 8])
head2 = create_using_list([1, 3, 4, 5])

display_ll(head1)
print()
display_ll(head2)
print()
final_head = merge_sorted_ll(head1, head2)
display_ll(final_head)
print()