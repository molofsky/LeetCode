# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        size = 0
        cur_node = head
        while cur_node != None:
            cur_node = cur_node.next
            size += 1
        
        if size == 1 and head != None:
            head.val = None
            head.next = None
            return
        i = 0
        prev_node = None
        cur_node = head
        while i < size - n:
            prev_node = cur_node
            cur_node = cur_node.next
            i += 1
        
        if cur_node.next != None:
            cur_node.val = cur_node.next.val
            cur_node.next = cur_node.next.next
        else:
            prev_node.next = None

        return head
        
        """
        Solution #2 

        head = ListNode(val=0, next=head)
        first = head
        second = head
        
        for _ in range(n + 1):
            first = first.next
        
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return head.next
        """
