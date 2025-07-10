def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    pre:ListNode=None
    cur:Listnode=head
    forw:Listnode=None
    while cur:
        forw=cur.next
        cur.next=pre
        pre=cur
        cur=forw
    return pre
    