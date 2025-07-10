def reverseList(self, head)
    pre:ListNode=None
    cur:Listnode=head
    forw:Listnode=None
    while cur:
        forw=cur.next
        cur.next=pre
        pre=cur
        cur=forw
    return pre
