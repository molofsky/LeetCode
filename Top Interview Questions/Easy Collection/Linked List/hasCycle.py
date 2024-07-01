# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        nodes = []
        curr = head
        while curr:
            if curr not in nodes:
                nodes.append(curr)
            else:
                return True
            curr = curr.next
        
        return False
            
            
        
        
