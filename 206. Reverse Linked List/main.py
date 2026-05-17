from typing import Optional

class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur = head
        temp = None
        prev = None 

        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev

if __name__ == "__main__":


    head: ListNode = ListNode(1) 
    head.next = ListNode(2)

    res = Solution()
    new_head = res.reverseList(head)

    assert new_head is not None
    print(new_head.val)
