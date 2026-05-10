# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lastNode = None
        presNode = head

        while presNode:
            nextNode = presNode.next
            presNode.next = lastNode
            lastNode = presNode
            presNode = nextNode
        return lastNode
