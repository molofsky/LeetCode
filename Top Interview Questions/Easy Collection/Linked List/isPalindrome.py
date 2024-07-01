# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head and not head.next:
            return True
        
        fast = head
        prev, curr = None, head
        while fast and fast.next:
            fast = fast.next.next
            
            node_next = curr.next
            curr.next = prev
            prev = curr
            curr = node_next
            
        if fast:
            curr = curr.next
        
        first_half, second_half = prev, curr
        while first_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        return True
            
        
        
