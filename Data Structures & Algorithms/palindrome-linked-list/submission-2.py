
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev,cur=None,slow
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        while prev and head:
            if prev.val!=head.val:
                return False
            prev=prev.next
            head=head.next
        return True        
                       