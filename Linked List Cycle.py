# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        f = head
        s = head
        while f and f.next:
            #print("f:  ",f.val)
            #print("n*n:  ",f.next.val)
            f = f.next.next
            s = s.next
            if(f==s):
                return 1
        return 0