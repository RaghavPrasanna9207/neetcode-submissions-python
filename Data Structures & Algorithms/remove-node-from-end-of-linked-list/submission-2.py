# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Complexities: O(n), O(1)
        # Traverse ahead n nodes with one pointer. After that, introduce the second pointer and traverse together. When the first reaches it's end, the second pointer's next node will be the one to be skipped.
        dummy = ListNode(0, head)
        left = dummy
        right = head

        for i in range(n):
            right = right.next

        while right:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next