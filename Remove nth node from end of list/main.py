import sys
from pathlib import Path
from typing import Optional

repo_root = Path(__file__).resolve().parents[1]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from python_ds.linked_list import ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        slow = fast = head

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return dummy.next



if __name__ == "__main__":
    sol = Solution()
    
    temp = ListNode(5)
    temp = ListNode(4, temp)
    temp = ListNode(3, temp)
    temp = ListNode(2, temp)
    head = ListNode(1, temp)

    ans = sol.removeNthFromEnd(head, 3)
    cur = ans 
    while cur:
        print(cur.val)
        cur = cur.next
