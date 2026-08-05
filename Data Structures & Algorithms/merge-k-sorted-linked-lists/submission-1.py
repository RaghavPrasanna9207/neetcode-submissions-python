# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    # Complexities: O(n log k), O(k)
    # Firstly, have a helper function to merge two lists. Then in the main function, have a while loop, under which a new list called 'mergedLists' is initialised. Here, have a for loop with steps of 2. This merges lists. After the for loop, set lists = mergedLists so that the for loop can happen again properly. Roughly: a b c d e, ab c d e, ab cd e is one iteration. Then, abcd e, abcde happens.
    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
                tail = tail.next
            else:
                tail.next = l2
                l2 = l2.next
                tail = tail.next

        if l1:
            tail.next = l1

        if l2:
            tail.next = l2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if len(lists) > i + 1:
                    l2 = lists[i + 1]
                else:
                    l2 = None
                mergedLists.append(self.mergeList(l1, l2))
            
            lists = mergedLists

        return lists[0]