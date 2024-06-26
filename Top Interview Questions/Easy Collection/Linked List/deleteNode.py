"""
There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before node should be in the same order.
All the values after node should be in the same order.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

"""
With the head included one solution could be

if node == head:
  node.val = node.next.val
  node.next = node.next.next
  return

prev_node = None
cur_node = head

while cur_node and cur_node != node:
  prev_node = cur_node
  cur_node = cur_node.next

if cur_node == node:
  prev_node.next = cur_node.next
  cur_node.next = None # optional clear the next pointer of the deleted node

"""
